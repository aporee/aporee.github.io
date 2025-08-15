# 🤖 KESA AI 챗봇

한국전기절감원(주)의 KESA 전력절감기 제품을 위한 AI 챗봇 상담 서비스입니다.

## ✨ 주요 기능

- **AI 기반 상담**: OpenAI GPT-3.5-turbo 모델 사용
- **맥락 이해**: 대화 기록을 기반으로 연속성 있는 상담
- **전문 지식**: KESA 제품에 대한 상세한 정보 제공
- **반응형 디자인**: 모바일/태블릿/데스크톱 지원
- **실시간 응답**: 빠른 AI 응답으로 고객 만족도 향상

## 🚀 배포 방법 (Vercel)

### 1단계: Vercel 계정 생성
1. [vercel.com](https://vercel.com) 방문
2. GitHub 계정으로 로그인
3. 새 프로젝트 생성

### 2단계: GitHub 저장소 연결
1. GitHub 저장소 선택 또는 새로 생성
2. 프로젝트 이름 설정 (예: `kesa-chatbot`)
3. 프레임워크 선택: **Other**

### 3단계: 환경변수 설정
1. 프로젝트 설정 → Environment Variables
2. 다음 변수 추가:
   ```
   OPENAI_API_KEY = your_openai_api_key_here
   ```
3. OpenAI API 키는 [OpenAI Platform](https://platform.openai.com)에서 발급

### 4단계: 배포
1. **Deploy** 버튼 클릭
2. 자동 배포 완료 대기
3. 배포된 URL 확인 (예: `https://kesa-chatbot.vercel.app`)

## 📁 프로젝트 구조

```
├── index.html              # 메인 페이지
├── chatbot.html            # 챗봇 페이지
├── api/
│   └── chat.py            # Vercel Python 서버리스 함수
├── requirements.txt        # Python 패키지 의존성
├── vercel.json            # Vercel 설정
├── package.json           # 프로젝트 설정
└── README.md              # 이 파일
```

## 🔧 기술 스택

- **프론트엔드**: HTML5, CSS3, JavaScript (ES6+)
- **백엔드**: Vercel Python 서버리스 함수
- **AI**: OpenAI GPT-3.5-turbo
- **호스팅**: Vercel (무료 플랜)

## 💰 비용

- **Vercel**: 무료 (월 100GB 트래픽, 100,000 함수 실행)
- **OpenAI**: 사용량에 따라 과금 (GPT-3.5-turbo: $0.002/1K tokens)

## 🎯 사용법

1. 챗봇 페이지 접속
2. 질문 입력 또는 퀵 버튼 클릭
3. AI가 자동으로 답변 생성
4. 대화 기록 유지로 맥락 이해

## 🔒 보안

- API 키는 Vercel 환경변수로 안전하게 관리
- 클라이언트에 API 키 노출되지 않음
- CORS 설정으로 안전한 API 호출

## 🚨 주의사항

- OpenAI API 키는 절대 GitHub에 업로드하지 마세요
- API 사용량 모니터링으로 예상치 못한 비용 방지
- 무료 크레딧 소진 시 유료 플랜으로 전환 필요

## 📞 지원

문제가 발생하거나 질문이 있으시면:
- GitHub Issues 등록
- 한국전기절감원(주) 연락처: 051-363-0458

## 📄 라이선스

이 프로젝트는 한국전기절감원(주)의 내부 사용을 위해 제작되었습니다.
