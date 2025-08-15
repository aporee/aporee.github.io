export default async function handler(req, res) {
  // CORS 설정
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  // OPTIONS 요청 처리 (preflight)
  if (req.method === 'OPTIONS') {
    res.status(200).end();
    return;
  }

  // POST 요청만 허용
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const { message, conversationHistory = [] } = req.body;

    // 메시지 유효성 검사
    if (!message || typeof message !== 'string') {
      return res.status(400).json({ error: 'Message is required and must be a string' });
    }

    // OpenAI API 호출
    const openaiResponse = await fetch('https://api.openai.com/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${process.env.OPENAI_API_KEY}`
      },
      body: JSON.stringify({
        model: 'gpt-3.5-turbo',
        messages: [
          {
            role: 'system',
            content: `당신은 한국전기절감원(주)의 KESA 전력절감기 제품 전문 상담사입니다. 
            
            주요 정보:
            - KESA는 산업용/상업용 전력절감기입니다
            - KESA-50, KESA-200, KESA-300 등 다양한 용량의 제품이 있으며, 전기료를 10% 이상 절감할 수 있습니다.
            - 전력 품질을 개선하고 전기료를 절감하는 첨단 전력절감 시스템입니다
            - AI 기반 원격 모니터링 기능도 포함되어 있습니다
            - 설치 기간: 2-4주
            - 연락처: 051-363-0458, 070-7771-6086
            - 주소: 부산광역시 사상구 사상로 453, 3층(모라동)
            
            친절하고 전문적으로 답변하되, 한국어로 대화하세요. 
            제품 문의, 설치 효과, 견적, 설치 과정 등에 대해 자세히 안내해주세요.`
          },
          ...conversationHistory,
          {
            role: 'user',
            content: message
          }
        ],
        max_tokens: 500,
        temperature: 0.7
      })
    });

    if (!openaiResponse.ok) {
      const errorData = await openaiResponse.json();
      console.error('OpenAI API Error:', errorData);
      return res.status(openaiResponse.status).json({ 
        error: 'OpenAI API 호출 실패',
        details: errorData 
      });
    }

    const data = await openaiResponse.json();
    const aiResponse = data.choices[0]?.message?.content || '죄송합니다. 응답을 생성할 수 없습니다.';

    // 응답 반환
    res.status(200).json({
      response: aiResponse,
      usage: data.usage
    });

  } catch (error) {
    console.error('Chat API Error:', error);
    res.status(500).json({ 
      error: '서버 내부 오류가 발생했습니다.',
      message: error.message 
    });
  }
}
