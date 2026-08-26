# Hotel Agent 5·6 + Literature RAG Judge

2026년 7월 24일 v8.2의 최신 Journey 기반 Agent 1~4 결과를 이어서 실행하는
2026년 8월 2일 통합 패키지입니다.

## 이번 버전에서 실제로 구현된 범위

1. Pilot 20
   - Gold 199 실행 결과와 최신 Gold 원문을 GL ID로 병합합니다.
   - 평점 층화와 부정 문제 포함 조건을 함께 사용해 고정된 20개를 선택합니다.
   - Agent 1~4에는 Gold Feature, Journey, Sentiment를 다시 입력하지 않습니다.
   - 리뷰 전체 원문은 20개 입력 파일에 보존합니다.

2. Agent 5 Rating Impact Analyzer
   - LLM이 아니라 재현 가능한 계산 코드입니다.
   - 예측 Feature × 예측 Journey 단위로 문제군을 집계합니다.
   - 전체 평균 별점, 문제군 부정 리뷰 평균 별점, 별점 하락, 부정 비율,
     표본 내 유병률과 대표 근거를 계산합니다.
   - 우선순위 공식은 다음과 같습니다.

        Priority = 100 × Negative Prevalence × Negative Rate
                   × Rating Drop / Observed Rating Range

   - 20개에서는 통계적 결론이 아니라 연결과 계산 검증에만 사용합니다.

3. Agent 6 Improvement Recommendation
   - 상위 문제군마다 최대 2개의 독립 개선조치를 생성합니다.
   - 한 행에는 한 조치만 들어갑니다.
   - 담당 부서, 실행단계, 적용시점, 기대효과, KPI, 실행 제약을 구조화합니다.
   - 완료된 문제군은 state 파일을 보고 건너뛰므로 중단 후 재개할 수 있습니다.

4. Literature RAG
   - PDF, DOCX, TXT, MD, CSV, XLSX 문헌을 읽습니다.
   - page 또는 sheet 위치를 유지한 청크를 만듭니다.
   - text-embedding-3-small 임베딩과 cosine similarity로 각 개선조치의
     상위 근거 청크를 검색합니다.
   - 문헌과 임베딩 설정이 같으면 캐시를 재사용합니다.

5. RAG LLM-as-a-Judge
   - 문헌 상태는 SUPPORTED, CONTRADICTED,
     INSUFFICIENT_EVIDENCE로 별도 저장합니다.
   - 개선안 품질은 Bhandari et al. (2026)의 8개 차원을 1~5점으로
     독립 채점합니다.
   - Actionability, Specificity, Feasibility, Expected Impact, Novelty,
     Non-redundancy, Bias, Reading Clarity를 사용합니다.
   - Composite 1~5는 여덟 점수의 산술평균입니다.
   - Composite 0~100은 100 × (Composite - 1) / 4입니다.
   - 검색 실패만으로 8개 품질점수를 자동 감점하지 않습니다.

6. CLEAN_HOTEL 1,000 확장
   - 7월 24일에 고정한 clean_hotel_1000_input.xlsx가 포함되어 있습니다.
   - 기존 v8.2 Dynamic Orchestrator 코드도 legacy_agent1_4_v8_2 폴더에
     원형대로 보존했습니다.
   - full1000 실행은 먼저 Agent 1~4를 재개 가능 방식으로 실행한 뒤,
     같은 Agent 5·6·RAG Judge 코드로 이어집니다.

## 입력 파일

- input/hotel_v8_199_regression_rag_judge.xlsx
- input/hotel_gold_label_200_guest_cycle_v8.xlsx
- input/clean_hotel_1000_input.xlsx
- input/CLEAN_HOTEL_SOURCE_MANIFEST.json

CLEAN_HOTEL의 전체 Arrow 원본은 약 100MB 이상이고, 1,000개 고정 표본에
필요한 행은 이미 input/clean_hotel_1000_input.xlsx에 모두 포함되어 있습니다.
따라서 원본 전체를 중복 복사하지 않고 출처와 파일 ID를 manifest에 기록했습니다.

## 먼저 키 없이 확인

패키지 폴더에서 의존성을 설치한 뒤 준비 실행을 확인합니다.

    python -m pip install -r requirements.txt

    python hotel_agent56_pipeline.py --mode pilot20 --prepare-only

이 명령은 API를 호출하지 않고 20개 선정, 원문 병합, Agent 5 계산,
8개 결과 템플릿 생성을 확인합니다.

## 키와 문헌이 준비된 뒤 20개 전체 실행

1. literature 폴더에 호텔 운영 개선안의 타당성과 효과를 검증할 문헌을 넣습니다.
2. OPENAI_API_KEY가 안전하게 연결된 환경에서 다음을 실행합니다.

    python hotel_agent56_pipeline.py --mode pilot20

기본 모델은 연구의 기존 설정을 유지합니다.

- Agent 6: gpt-5.4-nano
- Judge: gpt-5.4-mini
- Embedding: text-embedding-3-small

환경변수 AGENT6_MODEL, JUDGE_MODEL, EMBEDDING_MODEL로 교체할 수 있습니다.

## CLEAN_HOTEL 1,000 전체 실행

    python run_full1000_all.py --resume

이 명령은 다음 순서로 동작합니다.

1. CLEAN_HOTEL 1,000 전체 리뷰를 Agent 1~4에 review body only로 입력
2. 최신 J01~J04와 J00 보조값을 적용
3. 완료 리뷰를 저장하고 재실행 시 건너뜀
4. 1,000개 예측 결과로 Agent 5 집계
5. Agent 6 개선안 생성
6. 문헌 RAG와 8항목 Judge 실행

처음에는 비용 확인을 위해 다음처럼 일부만 점검할 수 있습니다.

    python run_full1000_all.py --limit 5 --agent14-only --resume

Agent 1~4의 일부 실행이 정상인지 확인한 뒤, 같은 출력 폴더를 재사용해
`python run_full1000_all.py --resume`으로 1,000개 전체와 후속 단계를 이어갑니다.

## 결과 파일

- 01_pilot20_input.xlsx 또는 01_full1000_input.xlsx
- 02_agent1_4_reused.xlsx
- 03_problem_clusters.xlsx
- 04_agent6_recommendations.xlsx
- 05_rag_retrieval.xlsx
- 06_rag_judge_results.xlsx
- 07_human_evaluation_template.xlsx
- 08_execution_log.xlsx

07_human_evaluation_template.xlsx의 Evaluator_1과 Evaluator_2를 독립적으로
채운 뒤 다음 명령으로 인간 평가자 간 QWK와 Human–Judge composite Spearman
상관을 계산할 수 있습니다.

    python validate_human_scores.py outputs/07_human_evaluation_template.xlsx outputs/06_rag_judge_results.xlsx

## 검증

    python -m pytest -q

테스트는 API를 호출하지 않으며 다음을 확인합니다.

- 20개 ID 고정 선택
- 모든 표본의 리뷰 전체 원문 존재
- Agent 5 우선순위 계산 범위
- 8개 Excel 결과 파일의 생성과 읽기

## 연구 근거

- Bhandari et al. (2026):
  https://arxiv.org/html/2601.12024v2
- OpenAI Structured Outputs:
  https://developers.openai.com/api/docs/guides/structured-outputs
- OpenAI Embeddings:
  https://developers.openai.com/api/docs/guides/embeddings

이 패키지는 Bhandari et al.의 8개 차원과 1~5 Likert 척도를 채택합니다.
세부 점수의 의미는 원 논문의 1 Poor, 2 Below Average, 3 Average,
4 Good, 5 Excellent를 사용합니다. 20개는 루브릭과 파이프라인 점검용이며,
Judge 신뢰성을 최종 확정하는 표본으로 해석하지 않습니다.

