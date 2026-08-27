# Project 01. LLM-Based Multi-Agent Service Quality Evaluation from Hotel Reviews

> **대표 연구 · Manuscript in Preparation**

호텔 리뷰 원문에서 서비스 문제의 근거를 찾고, Feature·Customer Journey·Sentiment·별점 영향을 거쳐 **호텔별 개선 우선순위와 실행 가능한 운영 조치**로 연결하는 Agentic AI 연구입니다.

단순한 리뷰 분류나 요약보다 결과의 생성 과정과 의사결정 근거를 다시 확인할 수 있는 구조에 초점을 두었습니다.

## 연구 질문

1. 어떤 서비스 문제가 어느 고객 여정에서 발생했는가?
2. 해당 문제가 별점 하락과 얼마나 관련되는가?
3. 호텔별로 무엇을 먼저 개선해야 하는가?
4. 개선안의 원문 근거와 Agent 판단 과정을 역추적할 수 있는가?
5. 동일 모델 조건에서 Single LLM과 Multi-Agent 구조의 품질·비용 차이는 무엇인가?

## 분석 구조

| 단계 | 역할 | 대표 출력 |
|---:|---|---|
| 1 | Evidence Extractor | 서비스 평가 근거 문장 |
| 2 | Feature Mapper | 호텔 서비스 Feature |
| 3 | Sentiment & Journey Scorer | 감성 방향과 고객 여정 |
| 4 | Final Verifier | 누락·과잉 분류 및 근거 일치 검증 |
| 5 | Rating Impact Analyzer | 부정 비율·별점 penalty·우선순위 |
| 6 | Improvement Recommendation | 담당 부서·실행 단계·KPI를 포함한 조치 |
| 평가 계층 | Literature RAG Judge | 문헌 근거와 출력 품질 평가 |

Gold label과 별점은 Agent 1–4의 입력으로 제공하지 않고 평가·후속 집계에만 사용했습니다. Agent 5는 재현 가능한 집계 코드로 구현하고, Agent 6와 RAG Judge는 구조화 출력 schema를 사용했습니다.

## 직접 구현한 핵심 요소

- Sequential·Feedback·Dynamic Orchestrator·Single LLM 비교 실험
- 199개 Gold 리뷰 검증과 1,000개 운영 표본 실행 구조
- `Hotel × Feature × Journey` 단위의 별점 영향과 호텔별 IPA
- 담당 부서·실행 단계·KPI·제약을 포함하는 개선안 schema
- 문헌 ingestion, embedding cache와 Literature RAG Judge
- JSONL 상태 파일, execution log, handoff trace와 fallback 기록
- `recommendation_id → impact_id → source_label_id → source_review_id` audit chain

## 대표 결과

- Gold 199개 기준 Multi-Agent의 Feature × Journey Macro Precision은 65.4%, Single LLM은 61.3%였습니다.
- Gold 우선순위와의 Spearman ρ는 Multi-Agent 0.868, Single LLM 0.785였습니다.
- Multi-Agent는 Gold Top 5를 5/5 보존했지만, Single LLM은 4/5를 보존했습니다.
- Single LLM은 호출·token·latency 비용이 크게 낮아, 구조 선택에는 정확도뿐 아니라 False Positive 비용과 처리비용을 함께 고려해야 했습니다.
- 1,321개 rating-impact 단위에서 생성된 8,258개 원시 action을 호텔별 IPA의 Q2 후보 18개로 압축해 실제 검토 가능한 수준으로 정리했습니다.

위 중요도와 penalty는 관찰된 리뷰·별점의 관련성을 이용한 우선순위 지표이며, 개선의 인과효과를 의미하지 않습니다.

## 저장소에서 확인할 수 있는 자료

### 코드와 실행 조건

- [Agent 5·6, RAG Judge와 결과 저장 파이프라인](src/hotel_agent56_pipeline.py)
- [1,000개 표본 전체 실행 orchestrator](src/run_full1000_all.py)
- [Python 의존성](requirements.txt)
- [2026-08-02 원본 패키지 README](docs/ORIGINAL_README_20260802.md)
- [2026-08-02 검증 기록](docs/VALIDATION_20260802.md)

### 연구 문서

- [2026-08-18 연구 발표자료](docs/research/2026-08-18-research-presentation.pptx)
- [전체 작업 인수인계·논문 Introduction](docs/research/research-handover-and-introduction.docx)
- [연구 방법론](docs/methodology/METHODOLOGY.md)
- [파이프라인 최적화 기록](docs/methodology/AGENT_PIPELINE_OPTIMIZATION.md)
- [Dynamic Orchestrator v8](docs/architecture/DYNAMIC_ORCHESTRATOR_V8.md)
- [구조 비교 v6](docs/architecture/ARCHITECTURE_COMPARE_V6.md)
- [구조별 Precision 비교 v7](docs/architecture/ARCHITECTURE_PRECISION_V7.md)

### 검증 데이터와 결과

- [Gold label 200·Guest Cycle v8 workbook](data/hotel_gold_label_200_guest_cycle_v8.xlsx)
- [199개 회귀검증·RAG Judge workbook](results/hotel_v8_199_regression_rag_judge.xlsx)
- [Dynamic Orchestrator 관리자 보고서](results/dynamic_orchestrator_manager_report.md)
- [Sequential 관리자 보고서](results/sequential_manager_report.md)
- [Pilot 요약 보고서](results/pilot_summary_report.md)
- [전체 결과 요약](docs/results/RESULTS.md)
- [Zero-cost 검증 결과](docs/results/ZERO_COST_RESULTS.md)
- [Agent 6 개선안 감사 기록](docs/validation/AGENT6_8258_AUDIT.md)
- [평가·개발·구조 비교 split](data/splits/)

## 파일 구성

```text
01-hotel-review-agentic-ai/
├── README.md
├── requirements.txt
├── src/                         # 실행 코드 2개
├── data/                        # Gold workbook과 split ID 3종
├── results/                     # 검증 workbook과 관리자 보고서
└── docs/
    ├── research/                # 발표자료·인수인계 문서
    ├── methodology/             # 방법론·최적화 기록
    ├── architecture/            # 구조 비교 문서
    ├── results/                 # 결과 해설
    └── validation/              # 감사·검증 기록
```

현재 이 폴더에는 README를 포함해 24개 파일이 있습니다. API key, `.env`, cache, 전체 실행 log, 중복·중간본과 19,561개 원본 리뷰 모집단은 포함하지 않았습니다.

전체 end-to-end 재실행에는 별도 문헌 폴더와 Agent 1–4 runner, 실제 API 환경이 추가로 필요합니다. 공개 파일의 선별 근거는 [Drive 자료 선별 인덱스](../../docs/DRIVE_SOURCE_INDEX.md)에서 확인할 수 있습니다.
