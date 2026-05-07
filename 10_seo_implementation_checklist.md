# SEO 구현 체크리스트 (개발자 전달용)

## 1. 기술 SEO 기반

### 1-1. URL·라우팅
- [ ] 모든 URL 영문 슬러그, 소문자, 하이픈 구분
- [ ] 301 리다이렉트 — 구 URL이 있다면 신 URL로
- [ ] Trailing slash 통일 (`/products/lab-pumps/` ✓)
- [ ] HTTPS 강제 (HTTP → HTTPS 301)
- [ ] www / non-www 통일 (canonical 설정)
- [ ] 한글 URL 회피 (cafe24·godomall 패턴 차별화)

### 1-2. 사이트맵·로봇
- [ ] `/sitemap.xml` 자동 생성 (제품·블로그·응용분야 모두 포함)
- [ ] `/robots.txt` — `/admin/`·`/cart/` 등 제외, `/sitemap.xml` 명시
- [ ] Google Search Console 등록 + 사이트맵 제출
- [ ] Naver 웹마스터 도구 등록 + 사이트맵 제출
- [ ] Bing Webmaster 등록 (선택)

### 1-3. 페이지 속도 (Core Web Vitals)
- [ ] LCP < 2.5초 (Hero 이미지 lazy + WebP/AVIF)
- [ ] FID < 100ms / INP < 200ms
- [ ] CLS < 0.1 (이미지 width/height 명시)
- [ ] 이미지 lazy loading (`loading="lazy"` 모든 이미지)
- [ ] CSS·JS 압축·번들링
- [ ] 폰트 `font-display: swap`
- [ ] CDN 사용 (Cloudflare 또는 자체)

### 1-4. 모바일 우선
- [ ] 반응형 단일 도메인 (m. 서브도메인 사용 안 함)
- [ ] viewport meta 설정
- [ ] 터치 타겟 최소 44×44px
- [ ] 모바일에서 가독성 폰트 16px 이상

## 2. On-Page SEO

### 2-1. 메타데이터 (모든 페이지)
- [ ] `<title>` 60자 이내, 메인 키워드 + 브랜드
- [ ] `<meta name="description">` 150자 이내
- [ ] `<link rel="canonical">` 설정
- [ ] OG 메타 (og:title·description·image·url·type·site_name)
- [ ] Twitter Card (summary_large_image)
- [ ] hreflang (ko / en 추후 분리 시)

### 2-2. HTML 시맨틱
- [ ] `<header>·<nav>·<main>·<section>·<article>·<aside>·<footer>` 사용
- [ ] H1 = 페이지 1개만, 메인 키워드 포함
- [ ] H2~H6 계층 정확히 (스킵 금지)
- [ ] `<button>` vs `<a>` 구분 (네비게이션은 a, 액션은 button)
- [ ] 이미지 alt 모두 작성 (한·영 키워드)
- [ ] 이미지 width/height 속성 명시

### 2-3. 키워드 배치
- [ ] H1에 메인 키워드 1회
- [ ] 본문 200자 이내 메인 키워드 1회
- [ ] 응용분야·F클러스터 키워드는 H2·본문에 자연스럽게
- [ ] 키워드 스터핑 금지 (밀도 2~3% 이내)

### 2-4. Schema.org 구조화 데이터
- [ ] 모든 페이지: BreadcrumbList
- [ ] 카테고리 랜딩: ItemList + Organization + FAQPage
- [ ] 시리즈/모델: Product + Brand + AggregateOffer
- [ ] 블로그: Article + Author + datePublished/Modified
- [ ] FAQ 섹션: FAQPage 스키마
- [ ] [Rich Results Test](https://search.google.com/test/rich-results) 검증 통과

## 3. Off-Page·콘텐츠

### 3-1. 백링크 자석 자료
- [ ] **호환성 매트릭스 PDF** (4사 빈틈, 인쇄·게시 자석)
- [ ] **MasterFlex 호환 매트릭스 PDF** (싸이스트 견제)
- [ ] **분주 정밀도 측정 보고서 PDF** (BT101L)
- [ ] **GMP 적합성 자료 PDF** (Tygon Pharmed)
- [ ] **유량 단위 환산기** (블로그 D9, 도구형)
- [ ] **시린지 호환 매트릭스 PDF** (TYD)

### 3-2. 외부 채널 (싸이스트·바이오컨비젼 학습)
- [ ] BRIC Bio마켓 등록 (바이오컨비젼 학습)
- [ ] 한국 실험실기기 디렉토리 등록
- [ ] YouTube 채널 — 작동 영상·셋업 가이드 (싸이스트 학습)
- [ ] 네이버 블로그 (운영 시 자체 도메인 백링크)
- [ ] 한국분석과학회·한국화학공학회 등 학술 디렉토리 (해당 시)

### 3-3. 콘텐츠 발행 일정
| Phase | 기간 | 콘텐츠 |
|---|---|---|
| 1a (1~3M) | 즉시 | 베스트셀러 튜브 페이지 3종 (#16·#15·2×1mm) |
| 1b (1~3M) | 즉시 | 호환성 매트릭스 페이지 + PDF |
| 1c (1~3M) | 1~3개월 | 응용분야 페이지 6개 |
| 2a (3~6M) | 3~6개월 | 블로그 D6 (Lead Fluid vs MasterFlex) |
| 2b (3~6M) | 3~6개월 | 시리즈/모델 페이지 풀 채움 |
| 2c (3~6M) | 3~6개월 | 블로그 D1·D2·D3·D9·D10 |
| 3 (6~12M) | 6~12개월 | 메인 키워드 1페이지 진입 |

## 4. 내부 링크 설계

### 4-1. 양방향 크로스링크 의무
- [ ] 카테고리 랜딩 → 5카드 → 시리즈 → 모델 (3층)
- [ ] 응용분야 ↔ 시리즈 ↔ 모델 (양방향)
- [ ] 모든 모델 페이지 → 호환성 매트릭스
- [ ] 블로그 D6 → BT101S/BT101L/BT600P/TYD
- [ ] 호환 튜브 페이지 → 사용 펌프 모델 역방향

### 4-2. anchor text 규칙
- [ ] anchor text에 키워드 포함 ("BT101S 자세히 보기" ✓ vs "여기 클릭" ✗)
- [ ] 동일 anchor text 중복 회피 (다양화)

### 4-3. orphan 페이지 금지
- [ ] 모든 페이지가 최소 1개 다른 페이지에서 링크 받아야 함
- [ ] 사이트맵 자동 검사 도구로 orphan 확인

## 5. 분석·트래킹

### 5-1. 분석 도구
- [ ] Google Analytics 4 설치
- [ ] Google Search Console 연결
- [ ] 네이버 애널리틱스 (선택)
- [ ] Microsoft Clarity (히트맵·세션 녹화) 설치
- [ ] 핫자(Hotjar) 또는 대안 (선택)

### 5-2. 전환 트래킹
- [ ] 견적 문의 폼 제출 → GA4 이벤트
- [ ] 카탈로그 PDF 다운로드 → GA4 이벤트
- [ ] 호환성 매트릭스 다운로드 → GA4 이벤트
- [ ] 위저드 4단계 완료 → GA4 이벤트
- [ ] 외부 링크 클릭 (블로그·SNS) → GA4 이벤트

### 5-3. 검색 트래픽 모니터링
- [ ] Search Console — 메인 키워드(A 클러스터) 순위 주간 추적
- [ ] F 클러스터(MasterFlex 호환) 순위 추적
- [ ] 응용분야(C 클러스터) 키워드 순위 추적
- [ ] 클릭률(CTR) 8% 미만 시 메타 설명 재작성

## 6. 보안·접근성

- [ ] HTTPS 인증서 (Let's Encrypt 또는 상용)
- [ ] HSTS 헤더
- [ ] CSP 헤더 (XSS 방어)
- [ ] WAI-ARIA 레이블 (스크린리더)
- [ ] 키보드 네비게이션 (모든 인터랙티브 요소)
- [ ] 색상 대비 WCAG AA (4.5:1 이상)
- [ ] alt text 모두 의미 있게 (장식용은 alt="" 명시)

## 7. 다국어 (Phase 3)

- [ ] 영문 사이트 분기 (`/en/`)
- [ ] hreflang 태그 (ko / en / x-default)
- [ ] 영문 키워드 매핑 (Peristaltic Pump·Syringe Pump)
- [ ] 영문 카탈로그 PDF
