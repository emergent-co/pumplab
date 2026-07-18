# GEO 로드맵 — 이어가기용 핸드오프 (최종 업데이트: 2026-07-18)

> **목적:** 다른 컴퓨터·새 세션에서 이 문서만 읽으면 그대로 이어갈 수 있게 한다.
> **대전제 1 — GEO 0순위:** GEO 최적화가 최우선(`OPERATIONS.md §0`). 모든 변경은 "GEO에 유리한가"를 먼저 통과.
> **대전제 2 — 무분별한 페이지 증식 금지:** 얇은 페이지 신설보다 **기존 페이지 보강**을 우선한다. GEO의 콘텐츠 확장은 "새 URL 남발"이 아니라 "기존 페이지를 깊게"로 달성한다. 통합·폐지는 되돌릴 수 있는 **301 리다이렉트**로.
> **워크플로:** 시작 전 `git pull` 필수 → 파일도구로 편집 → PowerShell `git add -A; git commit; git push`. 배포는 **Cloudflare Pages 자동**(빌드 명령 `python _build/build.py`, main 푸시 시 실행). GitHub Pages 워크플로는 실패해도 무시(꺼도 됨).

---

## 최근 개편 (2026-07-18)

**IA — 펌프 콘텐츠 /pump/ 하위 통합**
- nav: 리드플루이드를 **「펌프 A to Z」의 첫 하위**로 이동(최상단 단독 메뉴 폐지). FAQ `/pump/faq/`→`/faq/` 통합.

**무분별 증식 정리 — 14개 페이지 → 301 리다이렉트**
- 자동화 하우투 4(pc-control·flow-schedule·multi-pump-sync·run-log-csv) → `/requests/`
- 펌프·튜브 선택 2(pump-selection·tube-selection) → `/pump/select/`
- `/pump/faq/` → `/faq/`
- 산업·실험기법 7(cell-culture·chemostat·organ-on-chip·photobioreactor·medical-device-ivd → biopharmaceutical / industrial-chemical → flow-chemistry / food-beverage → environmental)
- 생존 응용 페이지: **biopharmaceutical · analytical-instrument · environmental · flow-chemistry + `/application/` 허브**
- 중앙 재배선 동기화: `CRAWLER_LINKS`·`static_pages`(build.py) · `posts.json` · `_redirects` · `site.js` nav

**리드플루이드 페이지 개편**
- 본문 = 벤토 카드 5개(스펙·유량계산기·소프트웨어·매뉴얼·A/S). 유량계산기·A/S는 **팝업(모달)**. A/S 폼 = 브랜드 선택 + 이메일, Formspree(`mnjkzppj`).
- 유량계산기: 튜브 규격(#·내경 mm) + 헤드 유형 + RPM 물리식 추정(출처 표기·캘리브레이션 안내).
- 매뉴얼: 모델 비교표(종류·유량·채널·RS485) + 바로가기 칩 + 카탈로그(하단).

**CT3001F 정정**
- "마그네틱/자기구동 기어펌프" → **PEEK 기어펌프(비자성)**로 사이트 전역 정정(모델 페이지·스키마·크롤러nav·llms.txt·pump/index). 유량 15~2700 mL/min.

---

## A. 완료 (라이브 확인됨)

**IA 정리**
- `셋업사례→도입·논문 사례` rename, 「실험별 셋업 가이드」→「실험 가이드」 통일(용어 충돌 해소)
- 3축 분리: **펌프 고를 때(선택)** / **실험 가이드(방법)** / **도입·논문 사례(증거)**
- 실험 가이드 허브 = 방법 5편만(선택 3종은 하단 링크로 분리)
- 리다이렉트 체인 제거(reviews→/setups/, tubing→tube-selection, recommend·recommend2→pump-selection)
- 구형 페이지 정리(leadfluid·inquiry noindex+redirect), 위저드(recommend.html) 결과 CTA를 나비엠알오/contact로
- 홈·가이드 CTA에 "나비엠알오에서 구매" + "제어 SW 무상·3년 A/S" 캡션

**GEO 구조 (build.py가 빌드 시 정적 주입 — 소스엔 마커만, 크롤러 가시화 목적)**
- `inject_static_nav()` — 전 페이지 푸터에 사이트 전체 링크(`CRAWLER_LINKS`) 정적 삽입
- `build_setups()` — /setups/ 논문 목록·정답블록 정적 렌더(마커 `<!--ST_CARDS_START-->` 등)
- `inject_head_schema()` — Organization/WebSite + 페이지별 **BreadcrumbList** JSON-LD를 `<head>`에 정적 주입(`ORG_WEBSITE_GRAPH`, `_breadcrumb_ld`)
- `normalize_html_urls()` — **main() 맨 마지막** 실행. 내부 `.html`을 제거해 clean URL(무확장자) 통일. canonical·og·링크·nav·스키마 전부 정리. sitemap도 `.replace('.html','')`
- `build_requests()` — /requests/ 개발요청 카드 정적 렌더

**콘텐츠 (SSOT = `_build/posts.json`)**
- 소프트웨어 moat 토픽 3편: pump-flow-schedule-ramp, multi-pump-sync-unattended, pump-run-log-csv-reproducibility (`type:guide`)
- 6대 응용분야(LeadFluid 공식 분류): biopharmaceutical, analytical-instrument, medical-device-ivd, environmental, industrial-chemical-material, food-beverage (`static_pages`)
- **도입·논문 사례 6편**(`type:setup`, 전부 LeadFluid 명시 원문 확인·인용문 포함):
  | 파일 | 모델 | 논문/저널 | 연구군 |
  |---|---|---|---|
  | brain-electrode-tyd01 | TYD01-01 시린지 | Nature Electronics 2024 | 바이오 |
  | catheter-heparin-bt101 | BT101 L 연동 | Nature Communications 2024 | 의료 |
  | co2-capture-ct3001f | CT3001F PEEK 기어 | Nature Communications 2024 | 에너지 |
  | heart-eshp-bt101l | BT101L 연동 | Frontiers Cardiovasc. Med. 2021 | **관류(장기)** |
  | damo-recirculation-bt600s | BT600S 연동 | Environ. Sci. Technol. 2021 | 환경 |
  | nitrification-ph-bq50s | BQ50S 정량 | Bioresource Technology 2017 | 환경 |
- 클러스터 상호링크: 관류 가이드↔심장논문, 환경 vertical↔환경논문 2편

**표현·기타**
- A/S 문구 "한국/국내 유일" → **"한국 공식 A/S 파트너"** 사이트 전체 통일(GBP 설명글도 동일)
- 나비엠알오 FAB 데스크톱(≥821px)만 ≈1.3배 확대(site.css)
- GA4 주요 이벤트 3종(navimro_click·generate_lead·file_download) 지정 완료
- 홈에 google+naver(388fb335…) 사이트 인증 정착
- llms.txt 새 IA로 재작성

---

## B. 반드시 지킬 규약

1. **새 콘텐츠 페이지 필수**: ① 질문형 롱테일 제목 ② 첫 문단 **정답블록(80~100자)** ③ JSON-LD(TechArticle+FAQPage, BreadcrumbList는 build.py 자동) ④ 내부 링크가 raw HTML에 존재 ⑤ 1페이지=1주제.
2. **SSOT**: 콘텐츠 메타는 `_build/posts.json`에만 추가(`type=setup|guide`). → 홈·검색·sitemap·/setups/ 목록 자동 반영. 유틸/분야 페이지는 `build.py`의 `static_pages`.
3. **신규 페이지는 `CRAWLER_LINKS`(build.py)에도 추가** — 안 하면 크롤러 nav에서 빠짐.
4. **도입·논문 사례 추가 규칙**: 본문에 "Lead Fluid"/"Leadfluid"가 **실제 명시**돼야 하고 **원문 인용문·DOI·모델** 필수. 못 찾으면 만들지 말 것(날조 금지). 논문이 다른 브랜드 펌프도 함께 쓰면 "LeadFluid가 담당한 역할만" 기술하고 출처 주석에 명기. 템플릿 = 기존 `setups/*.html`.
5. **검증은 배포 후 raw HTML** — `web_fetch`로 확인. **주의: web_fetch는 URL별로 캐시**하니, 이미 받아본 URL은 **`?v=날짜` 쿼리 붙여 캐시 우회**. (예: `https://rndsetup.com/setups/?v=0708`)
6. **마운트 지연 주의**: 샌드박스 bash가 파일도구 편집을 truncated/stale로 읽을 때가 많음(py_compile 오탐, JSON 오탐). **파일도구 Read가 authoritative.** build.py 로직 검증은 격리 스크립트로, 최종은 배포 후 web_fetch로.
7. **URL은 무확장자**가 정답(Cloudflare가 .html→무확장자 301). 새 canonical·링크는 소스에 .html로 써도 `normalize_html_urls`가 정리하지만, 가급적 무확장자로 통일.
8. **무분별한 페이지 증식 금지(대전제 2)**: 새 주제라도 얇으면 **기존 페이지 섹션으로 흡수**를 먼저 검토. 신설은 뚜렷한 롱테일·정답블록·상호링크가 성립할 때만. 통합·폐지는 **301 리다이렉트(체인 금지, 1홉 직결)**로 하고 `CRAWLER_LINKS`·`static_pages`·`posts.json`·`_redirects`·`site.js`를 함께 정리. 정기적으로 **실 인덱스 페이지 수**를 점검한다.

---

## C. 남은 작업 (우선순위)

### 1. 도입·논문 사례 확장 — 파일럿 연구군 커버 (임팩트 최대)
현재 6편이지만 파일럿 연구군 중 **관류 세포배양·연속배양(chemostat)·광배양·flow chemistry**엔 전용 논문이 아직 없음(심장 논문은 장기 관류라 근접).
- **RSC Lab on a Chip** (`10.1039/D0LC00493F`, 혈관신생 microfluidic, organ-on-chip/관류): 사장님이 PDF 보유. LeadFluid 명시 확인되면 organ-on-chip·관류 클러스터에 추가. (앞서 페이월로 미확인 → PDF로 검증 필요)
- chemostat/photobioreactor/flow-chemistry 연구군에서 LeadFluid 사용 논문 확보되면 각 가이드에 증거로 연결.
- 방법: PDF에서 `grep -i "lead *fluid"` 로 모델·인용문 추출 → 기존 setups 템플릿으로 페이지 생성 → posts.json + CRAWLER_LINKS + 해당 가이드 sd-related 양방향 링크.

### 2. (c) 나비엠알오 리스팅 문구 점검
실제 결제가 나비엠알오에서 일어나므로, 리스팅 제목·키워드·상세에 "제어 SW 포함·한국 공식 A/S·3년 보증"이 박혀 있는지 점검(navmro-review 스킬 활용). GEO(사이트)=인지, 나비엠알오 리스팅=전환.

### 3. 메뉴 pillar 재편 (item 7) — 신중, 큰 작업
콘텐츠 메뉴가 여러 개(논문사례/펌프고를때/소프트웨어제어/실험가이드+6분야). 응용(연구군/분야)을 pillar로 재정렬 검토. site.js NAV + 전 페이지 breadcrumb 동시 변경 → GA 효과 측정 후 결정.

### 4. (선택) 홈페이지 톤 정리
GBP용으로 정리한 "소프트웨어-우선 + 사실기반" 톤을 홈 카피에도 반영, 과장 표현(있으면) 점검.

---

## D. 매 작업 후 GEO 체크리스트
1. raw HTML(web_fetch, `?v=` 캐시우회)로 내부링크·정답블록·스키마가 JS 없이 보이는가?
2. 죽은 링크·리다이렉트 체인(2홉+) 없는가?
3. llms.txt·sitemap이 최신 IA와 일치?
4. posts.json SSOT 반영(홈 최신아티클·검색 자동)?
5. Rich Results Test로 FAQPage·BreadcrumbList 감지? (FAQ 리치결과는 구글이 폐지해 RRT에 안 떠도 정상 — Schema Markup Validator로 확인)

## E. 파일·경로 레퍼런스
| 역할 | 경로 | 메모 |
|---|---|---|
| 빌드 | `_build/build.py` | `CRAWLER_LINKS`, `static_pages`, `ORG_WEBSITE_GRAPH`, 5개 주입함수(nav/setups/head_schema/normalize/requests). main() 순서: build_setups→inject_static_nav→inject_head_schema→**normalize_html_urls(마지막)** |
| 콘텐츠 SSOT | `_build/posts.json` | `type=setup\|guide`, `noindex` 플래그. setup 6 + guide 6 |
| 공유 nav/footer/GA | `assets/site.js` | `NAV` 배열, `SEARCH_INDEX`. (Org/WebSite JSON-LD는 build.py로 이관됨) |
| 스타일 | `assets/site.css` | `sd-*`(상세) `ag-*`(가이드허브) `st-*`(논문허브) `sw-*`(비교표/쇼케이스) `ch-*`(크롬) `navimro-fab`(FAB) |
| 리다이렉트 | `_redirects` + 옛 html 스텁 | Cloudflare 서버 301, 무확장자 타겟 |
| AI 지도 | `llms.txt`, `robots.txt` | AI 크롤러 Allow |
| 원칙 | `OPERATIONS.md §0` | GEO 0순위 |
| 배포/검증 | Cloudflare Pages | 빌드 시 build.py 실행. 검증은 web_fetch `?v=` 캐시우회 |
