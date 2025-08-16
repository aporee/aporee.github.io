from http.server import BaseHTTPRequestHandler
import json
import os
import openai
from typing import Dict, List, Any

# OpenAI API 키 설정
openai.api_key = os.environ.get('OPENAI_API_KEY')

class ChatHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        """CORS preflight 요청 처리"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def do_POST(self):
        """POST 요청 처리 - AI 챗봇 응답 생성"""
        try:
            # CORS 헤더 설정
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-Type', 'application/json')
            
            # 요청 본문 읽기
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            request_data = json.loads(post_data.decode('utf-8'))
            
            # 메시지 유효성 검사
            message = request_data.get('message', '')
            conversation_history = request_data.get('conversationHistory', [])
            
            if not message or not isinstance(message, str):
                self.send_error_response(400, 'Message is required and must be a string')
                return
            
            # AI 응답 생성
            ai_response = self.generate_ai_response(message, conversation_history)
            
            # 성공 응답
            self.send_success_response(ai_response)
            
        except json.JSONDecodeError:
            self.send_error_response(400, 'Invalid JSON format')
        except Exception as e:
            print(f"Error in chat handler: {str(e)}")
            self.send_error_response(500, f'Internal server error: {str(e)}')
    
    def generate_ai_response(self, message: str, conversation_history: List[Dict[str, str]]) -> str:
        """OpenAI API를 사용하여 AI 응답 생성"""
        try:
            # 시스템 프롬프트 설정
            system_prompt = """당신은 한국전기절감원(주)의 KESA 전력절감기 제품 전문 상담사입니다.

주요 정보:
- KESA는 산업용/상업용 전력절감기입니다
- KESA-50, KESA-200, KESA-300 등 다양한 용량 제품
- 전기료 10% 이상 절감 효과
- AI 기반 원격 모니터링 기능
- 설치 기간: 2-4주
- 연락처: 051-363-0458, 070-7771-6086
- 주소: 부산광역시 사상구 사상로 453, 3층(모라동)

친절하고 전문적으로 답변하되, 한국어로 대화하세요.
제품 문의, 설치 효과, 견적, 설치 과정 등에 대해 자세히 안내해주세요."""

            # 메시지 구성
            messages = [
                {"role": "system", "content": system_prompt}
            ]
            
            # 대화 기록 추가
            messages.extend(conversation_history)
            
            # 사용자 메시지 추가
            messages.append({"role": "user", "content": message})
            
            # OpenAI API 호출
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=500,
                temperature=0.7
            )
            
            # 응답 추출
            ai_response = response.choices[0].message.content
            
            return ai_response
            
        except openai.error.OpenAIError as e:
            print(f"OpenAI API Error: {str(e)}")
            return "죄송합니다. AI 서비스에 일시적인 문제가 발생했습니다. 잠시 후 다시 시도해주세요."
        except Exception as e:
            print(f"Unexpected error in AI generation: {str(e)}")
            return "죄송합니다. 응답을 생성하는 중 오류가 발생했습니다."
    
    def send_success_response(self, response: str):
        """성공 응답 전송"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        
        response_data = {
            "response": response,
            "status": "success"
        }
        
        self.wfile.write(json.dumps(response_data, ensure_ascii=False).encode('utf-8'))
    
    def send_error_response(self, status_code: int, error_message: str):
        """에러 응답 전송"""
        self.send_response(status_code)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        
        error_data = {
            "error": error_message,
            "status": "error"
        }
        
        self.wfile.write(json.dumps(error_data, ensure_ascii=False).encode('utf-8'))

# Vercel 서버리스 함수 진입점
def handler(request, context):
    """Vercel 서버리스 함수 핸들러"""
    if request.method == 'POST':
        # 요청 데이터 파싱
        try:
            request_data = json.loads(request.body)
            message = request_data.get('message', '')
            conversation_history = request_data.get('conversationHistory', [])
            
            # AI 응답 생성
            ai_response = generate_ai_response(message, conversation_history)
            
            # 성공 응답 반환
            return {
                'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Content-Type': 'application/json'
                },
                'body': json.dumps({
                    "response": ai_response,
                    "status": "success"
                }, ensure_ascii=False)
            }
            
        except Exception as e:
            return {
                'statusCode': 500,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Content-Type': 'application/json'
                },
                'body': json.dumps({
                    "error": f"Internal server error: {str(e)}",
                    "status": "error"
                }, ensure_ascii=False)
            }
    
    # OPTIONS 요청 처리
    elif request.method == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': ''
        }
    
    # 지원하지 않는 메서드
    else:
        return {
            'statusCode': 405,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                "error": "Method not allowed",
                "status": "error"
            }, ensure_ascii=False)
        }

def generate_ai_response(message: str, conversation_history: List[Dict[str, str]]) -> str:
    """OpenAI API를 사용하여 AI 응답 생성 (독립 함수)"""
    try:
        # 시스템 프롬프트 설정
        system_prompt = """당신은 한국전기절감원(주)의 KESA 전력절감기 제품 전문 상담사입니다.

주요 정보:
- KESA는 산업용/상업용 전력절감기입니다
- KESA-50, KESA-200, KESA-300 등 다양한 용량 제품
- 전기료 10% 이상 절감 효과
- AI 기반 원격 모니터링 기능
- 설치 기간: 2-4주
- 연락처: 051-363-0458, 070-7771-6086
- 주소: 부산광역시 사상구 사상로 453, 3층(모라동)

친절하고 전문적으로 답변하되, 한국어로 대화하세요.
제품 문의, 설치 효과, 견적, 설치 과정 등에 대해 자세히 안내해주세요."""

        # 메시지 구성
        messages = [
            {"role": "system", "content": system_prompt}
        ]
        
        # 대화 기록 추가
        messages.extend(conversation_history)
        
        # 사용자 메시지 추가
        messages.append({"role": "user", "content": message})
        
        # OpenAI API 호출
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=500,
            temperature=0.7
        )
        
        # 응답 추출
        ai_response = response.choices[0].message.content
        
        return ai_response
        
    except openai.error.OpenAIError as e:
        print(f"OpenAI API Error: {str(e)}")
        return "죄송합니다. AI 서비스에 일시적인 문제가 발생했습니다. 잠시 후 다시 시도해주세요."
    except Exception as e:
        print(f"Unexpected error in AI generation: {str(e)}")
        return "죄송합니다. 응답을 생성하는 중 오류가 발생했습니다."

