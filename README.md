# 한국전기절감원(주) 웹사이트

지속가능한 친환경·저탄소 산업생태계 구축을 위한 전력절감 솔루션을 소개하는 웹사이트입니다.

## 🚀 Jekyll 기반 정적 사이트

이 웹사이트는 [Jekyll](https://jekyllrb.com/)을 사용하여 구축되었습니다.

### 주요 특징

- **중앙 집중식 정보 관리**: `_data/company.yml`에서 회사 정보를 관리
- **일관된 디자인**: 모든 페이지에 동일한 header와 footer 적용
- **SEO 최적화**: Jekyll SEO 태그를 통한 메타데이터 관리
- **GitHub Pages 호환**: 정적 호스팅에 최적화

## 🛠️ 개발 환경 설정

### 필수 요구사항

- Ruby 2.6.0 이상
- RubyGems
- GCC 및 Make

### 설치 및 실행

1. **의존성 설치**
   ```bash
   bundle install
   ```

2. **로컬 서버 실행**
   ```bash
   bundle exec jekyll serve
   ```

3. **빌드**
   ```bash
   bundle exec jekyll build
   ```

## 📁 프로젝트 구조

```
aporee.github.io/
├── _data/                    # 데이터 파일
│   └── company.yml          # 회사 정보
├── _layouts/                 # Jekyll 레이아웃
│   └── default.html         # 기본 레이아웃
├── assets/                   # 정적 자산
│   └── styles.css           # 공용 스타일
├── images/                   # 이미지 파일
├── _config.yml               # Jekyll 설정
├── Gemfile                   # Ruby 의존성
└── *.html                    # HTML 페이지들
```

## 🔧 데이터 관리

### 회사 정보 수정

`_data/company.yml` 파일을 수정하면 모든 페이지의 footer와 header에 자동으로 반영됩니다.

```yaml
# 연락처 정보 수정 예시
contact:
  phone:
    - "051-363-0458"
    - "070-7771-6086"
  fax: "051-363-0457"
```

### 페이지별 설정

각 HTML 파일의 front matter에서 페이지별 설정을 할 수 있습니다:

```yaml
---
layout: default
title: "페이지 제목"
description: "페이지 설명"
styles: |
  /* 페이지별 CSS */
scripts: |
  /* 페이지별 JavaScript */
---
```

## 🌐 배포

### GitHub Pages

이 저장소는 GitHub Pages에서 자동으로 빌드되고 배포됩니다.

### 로컬 테스트

```bash
# 로컬에서 빌드 테스트
bundle exec jekyll build

# 로컬 서버로 미리보기
bundle exec jekyll serve --livereload
```

## 📱 반응형 디자인

모든 페이지는 모바일과 데스크톱 환경에 최적화되어 있습니다:

- CSS Grid와 Flexbox를 활용한 레이아웃
- CSS 변수를 통한 일관된 디자인 시스템
- clamp() 함수를 사용한 반응형 타이포그래피

## 🔍 SEO 최적화

- 메타 태그 자동 생성
- Open Graph 태그 지원
- 구조화된 데이터 준비
- 사이트맵 자동 생성

## 📞 문의

웹사이트 관련 문의사항이 있으시면 연락주세요:

- **전화**: 051-363-0458, 070-7771-6086
- **팩스**: 051-363-0457
- **주소**: 부산광역시 사상구 사상로 453, 3층(모라동)

---

© 2025 KESA. All rights reserved.
