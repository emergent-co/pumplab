════════════════════════════════════════════════════════════
  셀렙 외부 제품 크롤러 — 사용 가이드
════════════════════════════════════════════════════════════

[ 무엇인가요? ]
시그마알드리치(성호씨그마)·코랩샵·올포랩 등 외부 사이트의
제품 페이지에서 제품명·가격·스펙·이미지 등을 자동 수집하여
CSV/JSON/HTML로 정리하는 도구입니다.

[ 누가 어디서 실행하나요? ]
영쨩님 PC에서 실행됩니다.
(셀렙 사이트 운영용 콘텐츠 정기 업데이트용)


══════════════════════════════════════════════════════════
  최초 1회 설치
══════════════════════════════════════════════════════════

1. Python 3.10 이상이 PC에 설치되어 있어야 합니다.
   설치 안 되어 있으면: https://www.python.org/downloads/
   ★ 설치 시 "Add Python to PATH" 체크 필수

2. install_requirements.bat 더블클릭
   (자동으로 requests, beautifulsoup4, lxml 설치)


══════════════════════════════════════════════════════════
  매번 사용 (3단계)
══════════════════════════════════════════════════════════

【 STEP 1 】urls.txt 열기 (메모장)
  - 크롤링하고 싶은 URL을 한 줄에 하나씩 입력
  - # 으로 시작하는 줄은 주석 (무시됨)
  - 예시:
      https://shsigma.co.kr/shop/PDNN18051800035
      https://shsigma.co.kr/shop/PDNN22061000021
      https://kolabshop.com/...

【 STEP 2 】run_crawl.bat 더블클릭
  - 자동으로 모든 URL 순차 크롤링
  - 진행 상황이 콘솔창에 표시됨
  - 각 URL당 약 1초 소요 (서버 부담 회피)

【 STEP 3 】결과 확인
  - products_output.csv  — 엑셀로 열어서 확인
  - products_output.json — HTML 사이트 자동 통합용
  - external_cards.html  — HTML 카드 스니펫 (붙여넣기용)
  - crawl_log.txt        — 실행 로그 (오류 확인)


══════════════════════════════════════════════════════════
  HTML 사이트에 카드 자동 추가하는 방법
══════════════════════════════════════════════════════════

1. external_cards.html 파일 열기
2. <div class="ext-products-grid"> ... </div> 부분 복사
3. tubing_curated_demo.html 또는 다른 페이지의 적절한 위치에 붙여넣기

또는 (자동화 진행 시):
  products_output.json을 사이트에서 fetch()하여 동적 렌더링


══════════════════════════════════════════════════════════
  지원 사이트 / 셀렉터 추가 방법
══════════════════════════════════════════════════════════

기본 지원 사이트:
  - shsigma.co.kr   (성호씨그마)
  - kolabshop.com   (코랩샵)
  - allforlab.com   (올포랩)
  - 기타 (OG 메타 태그로 자동 추출)

새 사이트 추가:
  crawl.py 파일의 SITE_SELECTORS 딕셔너리에 추가
    "newsite.co.kr": {
        "name": ['h1.product-title', ...],
        "price": ['.price-tag', ...],
        ...
    }


══════════════════════════════════════════════════════════
  자주 발생하는 문제
══════════════════════════════════════════════════════════

Q. "Python이 설치되어 있지 않습니다" 메시지
A. https://www.python.org/downloads/ 에서 Python 3.10+ 설치
   "Add Python to PATH" 체크 필수

Q. "ModuleNotFoundError: No module named 'requests'"
A. install_requirements.bat을 먼저 실행해 주세요.

Q. 일부 URL에서 "FAIL" 또는 빈 결과
A. (1) 해당 사이트가 봇 차단할 수 있음 (User-Agent 변경 시도)
   (2) HTML 구조가 다를 수 있음 (crawl.py의 셀렉터 수정 필요)
   (3) crawl_log.txt에서 정확한 에러 확인

Q. 한글이 깨져 보임
A. CSV는 UTF-8 BOM으로 저장되어 엑셀에서 정상 표시됨.
   메모장에서 안 깨지면 OK. 깨지면 인코딩 변경 필요.

Q. 가격이 "0원" 또는 빈값
A. 사이트에서 비회원에게 가격 미공개일 가능성.
   해당 사이트는 로그인 후 추출하거나, 가격은 수동 입력 필요.


══════════════════════════════════════════════════════════
  주의사항
══════════════════════════════════════════════════════════

★ 출처 표기 의무: 외부 사이트 정보 사용 시 반드시 출처 표기
★ 서버 부담 회피: 1초 대기로 자동 조절됨, 변경 금지
★ 저작권 존중: 시그마는 딜러에게 정보 공유 허용 명시 (괜찮음)
★ 가격 변동: 정기 업데이트 권장 (월 1회 정도)
★ 봇 차단 방지: 너무 빈번한 실행 자제


══════════════════════════════════════════════════════════
  웹 서버 모드 (Stage 2) — 버튼 한 번으로 재크롤
══════════════════════════════════════════════════════════

【 최초 1회 】
  install_requirements.bat 더블클릭
  (기존 의존성에 flask 추가 자동 설치)

【 매번 사용 】
  STEP 1: run_server.bat 더블클릭
   - 콘솔창에 "http://localhost:5000" 표시
   - 1~2초 후 브라우저가 자동으로 열림
     (수동으로 열려면: http://localhost:5000/tubing_curated_demo.html)

  STEP 2: 페이지 상단 노란 컨트롤 바
   - "🔄 지금 스크랩하기" 버튼 클릭
   - 콘솔창에 크롤링 진행 로그가 흐름
   - 완료되면 외부 제품 카드가 자동 갱신됨
   - 마지막 업데이트 시각 표시

  STEP 3: 종료
   - 콘솔창에서 Ctrl+C
   - 또는 콘솔창 X 버튼

【 라우트 】
  GET  /                       → tubing_curated_demo.html
  GET  /<파일명>               → 워크스페이스 정적 파일
  GET  /api/data               → products_output.json
  POST /api/refresh            → crawl.py 실행 후 결과 반환
  GET  /api/log                → crawl_log.txt (디버깅용)

【 정적 사용도 가능 (서버 없이) 】
  서버를 안 띄우고 file:// 로 열어도 카드는 표시됨.
  단, "지금 스크랩하기" 버튼은 작동하지 않음 (서버 필요).
  대신 run_crawl.bat 수동 실행 → 페이지 새로고침으로 갱신.


══════════════════════════════════════════════════════════
  변경 이력
══════════════════════════════════════════════════════════

2026-05-01 (Stage 2 — 동적 카드 + 미니 웹 서버)
  - server.py 신설 (Flask 기반 미니 서버)
    /api/data, /api/refresh, /api/log
  - run_server.bat 신설 (CRLF, 브라우저 자동 열기)
  - install_requirements.bat 에 flask 추가
  - tubing_curated_demo.html 변경:
    * 정적 외부 카드 4개 → <div id="extProducts"> 동적 렌더링
    * 컨트롤 바 추가 (상태 표시 + "지금 스크랩하기" 버튼)
    * fetch /api/data 실패 시 crawler/products_output.json 직접 fallback
    * file:// 환경에서도 카드 표시는 작동 (버튼만 비활성)
  - 카드는 옵션 2개 이상이면 가격 범위(₩A ~ ₩B 원) 표시



2026-05-01 (Phase C — 옵션 목록 추출)
  시그마 페이지의 옵션 테이블(품목 변형 N종) 추출 기능 추가
  - extract_options_shsigma() 함수 신설
  - <tr class="option_item"> 의 hidden input JSON 파싱
    (io_id, io_description, io_unit, io_price, io_price_dealer,
     io_price_real, io_stock_qty)
  - 출력 추가:
    JSON: options 배열 (옵션별 코드/이름/단위/가격/재고)
    JSON·CSV 공통: price_min, price_max, options_count
  - CSV에는 options 배열 자체는 안 넣음 (JSON 전용)
  - 카드 표시 예: 옵션 2개 이상 → "₩122,400 ~ ₩389,000"
                  옵션 1개      → "₩122,400"

2026-05-01 (Phase B 보정 — 접근성 숨김 텍스트 제거)
  같은 시범 URL 재검증 후 발견:
  - h2#sit_title 안에 <span class="sound_only">요약정보 및 구매</span>
    스크린리더용 텍스트가 함께 추출되어 노이즈 발생
  - safe_select_text에 .sound_only/.sr-only/.visually-hidden/[aria-hidden=true]
    제거 로직 추가 (copy 후 decompose 방식, 원본 soup 보호)
  - 시그마 가격 122,400원은 비로그인 공개 정가로 확인 → 그대로 사용

2026-05-01 (Phase A 셀렉터 보정 — 시그마)
  시범 URL: PDNN18052900028 1건 검증 후 다음 보정 적용
  - name: h2#sit_title 우선 (h1은 브레드크럼 노이즈 포함)
  - image: #sit_pvi_big img 우선 (시그마 og:image 없음)
  - price: tr.tr_price strong 우선 (실판매가, 옵션 첫번째 정가 회피)
  - spec: meta[name="description"] (시그마는 별도 스펙 없음)

2026-05-01 (.bat CRLF 변환)
  Q. 한글 메시지 깨지고 'nul', 'requests' 같은 단어가 명령어로 인식되는 에러
  A. .bat 파일이 LF로 저장되어 있어 발생. CRLF(\r\n)로 다시 저장 필요.
     (Notepad++ → 보기 → 줄 끝 표시 → "Windows" 선택 후 저장)


════════════════════════════════════════════════════════════
