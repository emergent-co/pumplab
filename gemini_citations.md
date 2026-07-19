# Gemini 인용 수집 로그 (rndsetup.com GEO 진단)

수집일: 2026-07-18 / 도구: Gemini 웹앱 (로그인 상태)

## 모델별 인용 메커니즘 (A/B 검증 결과)
- **Flash-Lite**: 실시간 웹 인용. 실제 웹페이지(The Pump Expert, Darwin Microfluidics, 캐시바이 등)를 칩으로 표기. → SEO·색인 싸움.
- **Pro**: 웹검색 안 함("실시간 웹 검색이 제한되어 있어"라고 직접 명시). 학습 데이터에서 브랜드를 꺼내고 출처는 제조사 공식사이트를 사후 부착. → 개체각인(entity salience) 싸움.

---

## 수집 데이터

| # | 그룹 | 모델 | 키워드 | 인용 출처 | rndsetup | 비고 |
|---|---|---|---|---|---|---|
| 1 | B | Flash-Lite | 연동펌프 유량이 설정값과 다른 이유 | The Pump Expert(3), Darwin Microfluidics, Atlantic Pumps, Saint-Gobain ICS | 없음 | 사이트에 동일 제목 페이지가 있는데 0회 |
| 2 | B | Pro | 연동펌프 유량이 설정값과 다른 이유 | 출처 없음 | 없음 | 출처 미강제 시 인용 안 함 |
| 3 | A | Pro | 실험실 정량펌프 추천 | 출처 없음. 브랜드: Masterflex, Watson-Marlow, KNF, ProMinent, SSI, LabAlliance | 없음 | 실험실 프레임(정확). 유통사 자리 없음 |
| 4 | A | Flash-Lite | 실험실 시린지펌프 추천 | Chemyx, Revodix(티스토리), Harvard Bioscience(2), TriContinent, WPI | 없음 | 개인 티스토리 블로그가 인용됨 — 주목 |
| 5 | A | Pro+출처강제 | 실험실 정량펌프 추천 | Harvard Apparatus, Chemyx 등 제조사 공식사이트 | 없음 | 출처를 강제해도 제조사 공식사이트만 |
| 6 | A | Flash-Lite | 실험실 연동펌프 추천 (이전 세션) | 캐시바이, Microlit USA, Aurora Pro Scientific, ELEXAN Scientific, Lead Fluid, ko.aliexpress.com | 없음 | 캐시바이 인용된 유일 사례 |
| 7 | A | Flash-Lite | 실험실 정량펌프 추천 (이전 세션) | Grundfos, PTCXPUMP, Sigma-Aldrich, ko.biolabequipments.com, Iwaki America, Iorric, Diener, PSG | 없음 | 산업 약품주입 프레임으로 이탈 |
| 8 | B | Flash-Lite | 연동펌프 튜브 교체 주기 | **Lead Fluid(5회)**, Aurora Pro Scientific(5), Darwin Microfluidics(4), Eagle Elastomer | 없음 | LeadFluid 본사 사이트가 다수 인용된 첫 사례 |
| 9 | C | Flash-Lite | 연동펌프를 PC로 제어하는 방법 | **인용 0개** | 없음 | 웹 근거 자체가 없는 빈 땅. Python 코드까지 생성 |
| 10 | C | Flash-Lite | 실험실 펌프 Modbus RS485 제어 소프트웨어 | Modbus Tools, Microsoft Store, GitHub, NModbus, Hamilton Company, Industrial Monitor Direct, LucidControl | 없음 | 펌프 업계가 아닌 범용 Modbus 도구가 인용됨 |
| 11 | D | Flash-Lite | 리드플루이드 LeadFluid 펌프 어떤가요 | Bio-Equip.cn(4), **티제이바이오앤셀(3)**, Lead Fluid(6) | 없음 | **경쟁사 티제이바이오앤셀이 한국어 브랜드 질의 인용을 점유.** 최대 격전지 |
| 12 | D | Flash-Lite | Masterflex 연동펌프 국내 대안 저렴한 제품 | 티스토리(2), 영진코퍼레이션(2), 덕산종합과학, 아토코리아, 바이오피앤에스 | 없음 | **사이트에 동일 목적 페이지(/compare/imported-peristaltic-alternative/) 존재하는데 0회.** 추천 대상은 프로넥스텍·영진·덕산·아토코리아 |
| 13 | E | Flash-Lite | 세포배양 관류 실험 펌프 셋업 방법 | Sigma-Aldrich(5), zeta biosystem(2), ibidi, Repligen, Microfluidics Innovation Center(2), Evotec | 없음 | 사이트에 관류배양 셋업 페이지 있으나 0회. 시약사·장비사가 점유 |
| 14 | A | Flash-Lite | 연구실용 연동펌프 가격과 구매처 | 코랩샵 KOLAB(5), 4science, 대영이화학, **올포랩(올포맵)**, 티스토리, 덕산종합과학, **티제이바이오앤셀**, 레보딕스 | 없음 | **구매·가격 의도에서 국내 과학기자재몰이 소환됨.** 올포랩 = 업로드 권한 보유. 나비엠알오는 미인용 |
| 15 | D | Flash-Lite | 중국산 연동펌프 A/S 믿을만한가요 | **인용 0개** | 없음 | **답변 내용이 실험셋업연구소 차별점과 정확히 일치**(국내 대리점·부품수급·기술지원·"단순 유통자인지"). 주인 없는 고의도 질의 |
| 16 | B | Flash-Lite | 연동펌프 튜브 찢어짐 원인과 해결 | Ruixiang Silicone(3), pinmotor.net(4), Kelair Pumps Australia(4), Thomson Process, Nanjing Runze Fluid | 없음 | **사이트에 동일 제목 페이지(/pump/atoz/tubing-crush-tear-causes/) 존재하는데 0회.** 전부 해외(중국·호주) 업체 |
| 17 | C | Flash-Lite | 실험실 펌프 여러대 동시 제어와 무인 장시간 운전 | **인용 0개** | 없음 | C그룹 3연속 인용 0. 워치독·로그기록·이중화 등 실험셋업연구소 SW 기능과 내용 일치 |

---

## 2차 수집 — 실제 구매 검토자 질의 (2026-07-18, Flash-Lite)

기존 조사가 "자사 페이지 제목 그대로 친 질의"라는 비판(루프4)을 받아, 실제 구매자가 칠 법한 자연어 질문으로 재수집.

| # | 카테고리 | 키워드 | 인용 출처 | rndsetup | 비고 |
|---|---|---|---|---|---|
| 18 | 시린지 | 동물실험용 시린지펌프 추천해주세요 | Syrris, Instech Laboratories(5), **Revodix-티스토리(4)**, Ossila, Chemyx | 없음 | 국내 유통사 레보딕스가 티스토리로 4회. "국내 유통사(예: 레보딕스) 데모 체험" 본문 언급까지 획득 |
| 19 | 시린지 | 미세유체 칩 실험 맥동 없는 시린지펌프 모델 | Darwin Microfluidics(4), Ossila(3), Revodix-티스토리, World Precision Instruments | 없음 | NE-1000X, Vindum, UniGo 등 구체 모델 추천 |
| 20 | 기어 | 유기용매 이송용 PEEK 기어펌프 내성 괜찮을까요 | Iorric, MICROSOLV, Atlas Fibre(5), cplabsafety.com(2), VICI Precision Sampling, First Mold | 없음 | 소재 정보 사이트가 점유. 펌프 유통사 없음 |
| 21 | 방폭 | 인화성 용매 이송할때 방폭 펌프 꼭 써야 하나요 | QEEHUA PUMP, PROAnalytics(2), Multi Torque Industries(5), GODO PUMPS(3), VWR(2) | 없음 | 산업 펌프사·안전규정 중심. 실험실 맥락 부재 |
| 22 | 정량/배양 | 배양기 배지 자동 공급 펌프 어떤걸 써야 하나요 | **인용 0개** | 없음 | 연동펌프를 1순위로 추천. 브랜드는 Cole-Parmer, **Kamoer**(중국 경쟁사). 리드플루이드 미언급 |
| 23 | 구매실무 | 연구비로 실험장비 구매할때 규격서 작성 어떻게 하나요 | **인용 0개** | 없음 | 국가연구비 구매 프로세스. 장비사 개입 여지 있으나 아무도 콘텐츠 없음 |
| 24 | 정량/pH | pH 조절용 정량펌프 산 염기 투입 어떤 제품 써야하나요 | JENSPRIMA(2), Newater(6), PSM 공정안전관리, almawatech(2) | 없음 | **수처리 산업 프레임으로 이탈**(#7과 동일 패턴). 브랜드는 Grundfos·Milton Roy·ProMinent·SEKO |
| 25 | 구매실무 | 실험실 펌프 견적 어떻게 받나요 대리점 비교 | **코랩샵 KOLAB(6)**, Global Pumps(4), Suofu(2) | 없음 | 본문에 "온라인 전문몰: 코랩(KOLAB), **레보딕스(Revodix)**, 동방하이테크상사" 실명 노출. "A/S 보증기간·소모품 수급을 문서로 확인하라"는 조언 = 자사 강점과 일치 |
| 26 | 구매실무 | 실험실 펌프 A/S 보증기간 보통 얼마나 되나요 | www.kca.go.kr(2), World Precision Instruments(3), Fruitland Manufacturing(2), 윌로펌프, BRANDTECH Scientific | 없음 | **"기본 1년, 브랜드별 1~3년"** — 자사 3년 무상보증이 시장 최상단임을 AI가 스스로 증명. 답변이 대리점에 물어볼 질문 4개를 제시(보증개월·소모품포함·연장프로그램·부품재고) 전부 자사가 유리하게 답할 수 있는 항목 |
| 27 | 기술선택 | 연동펌프랑 시린지펌프 중에 어떤걸 고르는게 맞나요 | **인용 0개** | 없음 | 비교표 생성. ※주의: 새 채팅 버튼이 안 눌려 이전 pH 대화에 이어짐 → **맥락 오염 발생**. 이 건은 독립 관측치로 쓸 수 없음 |

| 28 | 구매실무 | 실험실 펌프 나라장터 조달 구매 가능한가요 | **인용 0개** | 없음 | **"조달 등록이 안 돼 있으면 공급업체에 나라장터 종합쇼핑몰 제품 등록을 요청하거나 수의계약 가능 여부를 문의하라"** — 공공기관 고객이 실험셋업연구소에 요구할 행동을 AI가 지시. 나라장터 등록이 곧 매출 경로 |
| 29 | 기술선택 | 점도 높은 액체 이송 실험실 펌프 추천 | ARO Pumps(6) | 없음 | 산업 공압펌프사 단독 점유. 브랜드 추천은 KNF·Cole-Parmer·Iwaki |

### 2차 수집 방법론 한계
- 27건 중 새 채팅 분리에 실패한 건이 최소 1건(#27) 있음. UI 좌표가 창 크기에 따라 바뀌어 발생.
- 재현 측정 여전히 0회. 단일 계정·로그인 상태.
- 따라서 아래 비교는 "경향"이며 통계적 결론이 아님.

---

## 29건 종합 (1차 17 + 2차 12)

**rndsetup.com 인용: 29건 중 0건.** 카테고리를 연동·시린지·기어·방폭·구매실무로 넓혀도 동일.

### 프레임 이탈 규칙 (재현 확인됨)
"정량펌프"는 한국어 웹에서 **수처리 약품주입 용어**. `실험실 정량펌프 추천`(#7)과 `pH 조절용 정량펌프`(#24) 두 건 모두 Grundfos·ProMinent·Newater 등 수처리 프레임으로 이탈.
→ 반면 `배양기 배지 자동 공급 펌프`(#22)는 즉시 연동펌프를 1순위 추천.
**결론: "정량"이 아니라 용도어(배양·분주·미세유체)나 형식어(연동·시린지)로 콘텐츠를 잡아야 함.**

### 인용 0 질의의 성격 (총 8건)
#9, #15, #17, #22, #23, #27, #28 + 일부. 공통점: **서술형·절차형·판단기준형 질의**. 고유명사(Modbus, RS485, PEEK, 방폭)가 들어가면 검색이 켜짐.

### 국내 경쟁자 인용 지도
| 경쟁자 | 인용된 질의 | 채널 |
|---|---|---|
| 코랩샵 KOLAB | #14 가격·구매처(5), #25 견적(6) | 자사몰 |
| 레보딕스 Revodix | #14, #18 시린지(4), #19, #25 본문언급 | **티스토리 블로그** |
| 티제이바이오앤셀 | #11 브랜드질의(3), #14 | 자사몰 |
| 영진·덕산·아토코리아 | #12 Masterflex 대안 | 자사몰 |
| 올포랩 | #14 | 자사몰 (업로드 권한 보유) |

### 자사 강점이 답변에 직접 등장한 사례
- #26 A/S 보증: **"기본 1년, 브랜드별 1~3년"** → 자사 3년은 시장 최상단
- #26: 대리점에 물어볼 4개 질문(보증개월·소모품포함·연장·부품재고) 전부 자사 유리
- #25 견적: "A/S 보증기간·소모품 수급을 문서로 확인하라"
- #15 중국산 A/S: "단순 유통자인지 기술 대응 능력이 있는지"
- #28 나라장터: "공급업체에 종합쇼핑몰 제품 등록을 요청하라"

## 그룹별 패턴 (17개 수집 시점)

- **A 구매의도**: 국내 과학기자재몰 소환됨 (코랩샵 KOLAB, 4science, 올포랩, 대영이화학, 덕산종합과학). 캐시바이는 연동펌프 키워드에서만. 나비엠알오는 한 번도 인용 안 됨.
- **B 문제해결**: 사이트에 동일 제목 페이지가 있는 3개 키워드 전부 0회. 해외 제조사·유통사(The Pump Expert, Kelair, Ruixiang, pinmotor)가 점유. → 콘텐츠가 아니라 권위·색인 문제 확정.
- **C 제어·자동화**: 3개 중 **2개가 인용 0**(#9 서술형, #17 서술형), **1개는 인용 7개**(#10 "Modbus RS485" — 고유명사 포함). → 수요 부재가 아니라 **검색 트리거 부재**. 고유명사가 들어가면 검색이 켜짐. (초기 요약에서 "3연속 0"으로 잘못 적었던 것을 정정)
- **D 브랜드**: 리드플루이드 브랜드 질의를 **경쟁사 티제이바이오앤셀**이 점유. Masterflex 대안 질의도 국내 경쟁 유통사들이 점유. "중국산 A/S" 질의는 인용 0.
- **E 셋업**: 시약사(Sigma-Aldrich)·장비사(ibidi, Repligen)가 점유.

