# 정보 구조 (Information Architecture)

## 사이트 트리 (3층 강제)

```
celleb.co.kr/  (홈)
│
├─ /products/  (제품 카탈로그 허브)
│  └─ /products/lab-pumps/  ★ 카테고리 랜딩 (메인 키워드)
│     │
│     ├─ /peristaltic-variable/  (속도가변형)
│     │  ├─ /bq80s/
│     │  ├─ /bt103s/
│     │  ├─ /bt101s/  ★ 시리즈 페이지
│     │  │  ├─ /bt101s-dgds-6/
│     │  │  ├─ /bt101s-dgds-10/
│     │  │  ├─ /bt101s-dt10/
│     │  │  ├─ /bt101s-yz15t/  ★ 모델 상세 (베스트)
│     │  │  └─ /bt101s-yt25/
│     │  ├─ /bt301s/
│     │  └─ /bt601s/
│     │
│     ├─ /peristaltic-intelligent/  (지능형·분주)
│     │  ├─ /bt101l/  ★ 시리즈 페이지
│     │  │  ├─ /bt101l-dgds/
│     │  │  ├─ /bt101l-dt10/
│     │  │  ├─ /bt101l-yz15t/  ★ 모델 상세
│     │  │  └─ /bt101l-yt25/
│     │  ├─ /bt301l/  /bt601l/
│     │  ├─ /bt101f/  /bt301f/  /bt601f/
│     │  └─ /bt600p/
│     │
│     ├─ /gear/  (정밀 기어펌프)
│     │  ├─ /ct3001s/  (MG204·MG209·MG213)
│     │  └─ /ct3001f/
│     │
│     ├─ /syringe-integrated/  (시린지 일체형)
│     │  ├─ /tys/
│     │  └─ /tyd/  ★ 시리즈 페이지
│     │     ├─ /tyd01-01/  ★ 모델 상세
│     │     ├─ /tyd01-02/
│     │     ├─ /tyd02-01/  /tyd02-02/  /tyd02-04/  /tyd02-06/  /tyd02-10/
│     │     └─ /tyd03-01/
│     │
│     └─ /syringe-split/  (시린지 스플릿)
│        ├─ /tfd-integrated/
│        └─ /tfd04-zx/
│
├─ /accessories/  (소모품 허브)
│  ├─ /tubing/  (튜브 카탈로그)
│  │  ├─ /silicone/  (소재 카테고리)
│  │  │  ├─ /silicone-13/  ~ /silicone-25/  (호수별 18종, 베스트셀러는 풀 페이지)
│  │  │  ├─ ★ /silicone-16/  (#16 베스트셀러)
│  │  │  ├─ ★ /silicone-15/  (#15 베스트셀러)
│  │  │  └─ ★ /silicone-2x1/  (2×1mm 베스트셀러)
│  │  ├─ /tygon-pharmed/  (GMP)
│  │  ├─ /tygon-chemical/  (내약품)
│  │  ├─ /tygon-s3/  (식품)
│  │  └─ /viton-f5500/  (강산·유기용매)
│  ├─ /syringe/  (시린지 카탈로그)
│  │  ├─ /micro/  (10·25·50μL)
│  │  ├─ /sub-ml/  (100·250·500μL)
│  │  ├─ /standard/  (1·5·10mL)  ★
│  │  ├─ /large/  (30·60mL)
│  │  ├─ /gas-tight/  ★ (가스타이트)
│  │  ├─ /glass/
│  │  └─ /plastic/
│  └─ ★ /compatibility/  (호환성 매트릭스 — 4사 빈틈)
│
├─ /applications/  ★ 응용분야 허브 (4사 빈틈)
│  ├─ /cell-culture/  (세포배양)
│  ├─ /hplc/  (HPLC·분석)
│  ├─ /pharma-gmp/  (제약·GMP)
│  ├─ /food-beverage/  (식품·음료)
│  ├─ /chemical/  (화학·내약품)
│  └─ /microfluidics/  (마이크로 정량주입)
│
├─ /resources/  (자료실)
│  ├─ /catalog/  (카탈로그 PDF)
│  ├─ /manual/  (매뉴얼 PDF)
│  └─ /compat/  (호환성 자료)
│
├─ /blog/  (기술 블로그)
│  ├─ /peristaltic-principle/  (D1)
│  ├─ /pump-comparison/  (D2)
│  ├─ /tube-selection-guide/  (D3)
│  ├─ /tubing-material/  (D4)
│  ├─ /syringe-precision/  (D5)
│  ├─ ★ /leadfluid-vs-masterflex/  (D6 — 핵심 자석)
│  ├─ /gmp-pump-criteria/  (D7)
│  ├─ /cell-culture-automation/  (D8)
│  ├─ /flow-unit-converter/  (D9 — 도구형)
│  ├─ /pump-head-guide/  (D10)
│  ├─ /masterflex-alternative/  (F1)
│  ├─ /cole-parmer-alternative/  (F2)
│  ├─ /leadfluid-vs-masterflex-price/  (F7)
│  └─ /watson-marlow-alternative/  (F11)
│
├─ /contact/  (문의)
│  ├─ /quote/  (견적 폼)
│  └─ /support/  (A/S 폼)
│
├─ /about/  (회사소개)
└─ /privacy/  /terms/  /sitemap/
```

## 3층 깊이 강제 원칙

| 층 | 페이지 유형 | 키워드 노출 |
|---|---|---|
| 1층 | 카테고리 랜딩 | 메인 키워드 + 응용분야 + MasterFlex 호환 |
| 2층 | 시리즈 페이지·소재 카테고리 | 시리즈명 + 응용 |
| 3층 | 모델 상세·호수별 페이지 | 모델 코드 + 정확 사양 |

## 응용분야↔제품 양방향 크로스링크

```
/applications/cell-culture/  ←→  BT101L-YZ15T, BT101S-YZ15T, BT600P, TYD01-01
/applications/hplc/         ←→  TYD01-01, CT3001S, CT3001F, BT101S-DG/DS
/applications/pharma-gmp/   ←→  BT600P, BT101L, Tygon Pharmed BPT
/applications/food-beverage/ ←→ BT101L-YZ15T, Tygon S3
/applications/chemical/      ←→ Viton F-5500, Tygon Chemical, BT101L-YZ15T, CT3001
/applications/microfluidics/ ←→ TYD01-01, TYD02-01, TFD, CT3001S
```

## 호환성 매트릭스 — 도메인 권위 집중점

```
모든 본체 페이지   ─┐
모든 튜브 페이지   ─┼─→ /accessories/compatibility/  (PDF 다운로드)
모든 시린지 페이지 ─┘                      │
                                            └─→ 자연 백링크 (인쇄·게시)
```

## URL 명명 규칙

- 모두 소문자, 하이픈 구분
- 영문 슬러그 (한글 슬러그 회피 — godomall·cafe24와 차별화)
- 짧고 의미 명확 (`/bt101s-yz15t/`)
- 깊이 4단계까지 허용 (`/products/lab-pumps/peristaltic-variable/bt101s/`)

## 사이트맵 XML 우선순위

| URL 패턴 | priority | changefreq | 비고 |
|---|---|---|---|
| / | 1.0 | weekly | |
| /products/lab-pumps/ | 1.0 | weekly | 메인 키워드 랜딩 |
| /applications/* | 0.9 | monthly | 4사 빈틈 차별화 |
| /accessories/compatibility/ | 0.9 | monthly | 백링크 자석 |
| /products/lab-pumps/peristaltic-variable/* | 0.8 | monthly | BT101S 등 (수요 大) |
| /products/lab-pumps/peristaltic-intelligent/* | 0.8 | monthly | BT101L 등 (수요 大) |
| /products/lab-pumps/syringe-integrated/* | 0.8 | monthly | TYD 등 (수요 大) |
| /products/lab-pumps/gear/* | 0.7 | monthly | 정밀 기어 (수요 中) |
| **/products/lab-pumps/syringe-split/*** | **0.6** | monthly | **★ 카드 E 축소: SKU 6개로 가장 작아 우선순위 낮춤** |
| /accessories/tubing/silicone-16/ 등 베스트셀러 | 0.8 | monthly | |
| /products/lab-pumps/*/*/  (모델 상세) | 0.7 | monthly | |
| /blog/* | 0.6 | monthly | |
| /resources/* | 0.5 | yearly | |
