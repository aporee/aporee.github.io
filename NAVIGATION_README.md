# 네비게이션 바 표준화 가이드

## 📁 파일 구조
- `navigation.html` - 표준화된 네비게이션 바 HTML
- `navigation.css` - 네비게이션 바 CSS 스타일
- `NAVIGATION_README.md` - 이 가이드 문서

## 🔧 사용법

### 1. 새로운 페이지에 네비게이션 추가
1. `navigation.html` 파일을 열어서 `<nav>` 태그 전체를 복사
2. 새 페이지의 `<header>` 태그 안에 붙여넣기
3. `navigation.css`의 스타일을 페이지의 `<style>` 태그에 복사

### 2. 네비게이션 메뉴 수정
1. `navigation.html` 파일에서 메뉴 항목 수정
2. 모든 페이지의 네비게이션 부분을 새 내용으로 교체
3. 경로 확인 (폴더 위치에 따라 `./` 또는 `../` 사용)

### 3. 네비게이션 스타일 수정
1. `navigation.css` 파일에서 스타일 수정
2. 모든 페이지의 `<style>` 태그에 새 스타일 복사

## 📂 경로 규칙

### 루트 폴더의 페이지들
```html
<a href="./about.html">회사소개</a>
<a href="./power-consulting.html">전력컨설팅</a>
```

### 하위 폴더의 페이지들
```html
<!-- products/ 폴더에서 -->
<a href="../about.html">회사소개</a>
<a href="../power-consulting.html">전력컨설팅</a>

<!-- cases/ 폴더에서 -->
<a href="../about.html">회사소개</a>
<a href="../power-consulting.html">전력컨설팅</a>
```

## 🚀 업데이트 워크플로우

### 네비게이션 메뉴 변경 시:
1. `navigation.html` 수정
2. 다음 명령어로 모든 HTML 파일 찾기:
   ```bash
   find . -name "*.html" -not -path "./en/*"
   ```
3. 각 파일의 `<nav class="menu">` 부분 교체

### 네비게이션 스타일 변경 시:
1. `navigation.css` 수정
2. 모든 HTML 파일의 `<style>` 태그에 스타일 복사

## 📝 현재 네비게이션 구성

```html
<nav class="menu" aria-label="주요 메뉴">
  <a href="./about.html">회사소개</a>
  <a href="./power-consulting.html">전력컨설팅</a>
  <a href="./products/index.html">제품소개</a>
  <a href="./effects.html">설치효과·특성</a>
  <a href="./cases/index.html">시공사례</a>
  <a href="./contact.html">문의하기</a>
</nav>
```

## ⚠️ 주의사항

1. **경로 확인**: 페이지 위치에 따라 상대 경로 조정 필수
2. **스타일 충돌**: 기존 스타일과 충돌하지 않는지 확인
3. **접근성**: `aria-label` 속성 유지
4. **반응형**: 모바일 환경에서도 정상 작동하는지 확인

## 🔍 검증 방법

1. 브라우저에서 모든 페이지의 네비게이션 테스트
2. 링크가 올바른 페이지로 이동하는지 확인
3. 모바일 환경에서 메뉴가 정상 표시되는지 확인
4. 스타일이 일관되게 적용되는지 확인

