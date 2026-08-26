# Project 01. LLM-Based Multi-Agent Service Quality Evaluation from Hotel Reviews

*호텔 리뷰 기반 LLM 멀티에이전트 서비스 품질평가*

호텔 리뷰 원문을 단계별로 분석해 서비스 문제를 식별하고, 별점 영향과 실행 가능한 운영 개선안까지 연결하는 Agentic AI 연구 프로젝트입니다. 핵심 목표는 LLM의 최종 답변만 얻는 것이 아니라 **판단 근거·단계 간 전달·계산식·실패 기록을 다시 추적할 수 있는 평가 workflow**를 만드는 것이었습니다.

## 문제 정의

일반적인 리뷰 분석은 감성 점수나 토픽 요약에서 끝나기 쉽습니다. 이 프로젝트에서는 다음 질문을 함께 다뤘습니다.

1. 리뷰의 어떤 서비스 특징이 어느 고객 여정에서 문제였는가?
2. 그 문제가 별점 하락과 얼마나 연결되는가?
3. 호텔 관리자가 실제로 실행할 수 있는 조치로 어떻게 변환할 것인가?
4. 개선안의 품질과 문헌 근거를 어떻게 분리해 평가할 것인가?
5. Agent 구조에 따라 성능·비용·추적성이 어떻게 달라지는가?

## 6단계 분석 구조

| 단계 | 역할 | 구현 성격 |
|---:|---|---|
| 1 | Feature Extractor | 리뷰에서 서비스 특징 예측 |
| 2 | Customer Journey Classifier | 문제 발생 고객 여정 예측 |
| 3 | Sentiment Analyzer | 감성·서비스 실패 여부 예측 |
| 4 | Evidence Selector | 판단을 뒷받침하는 근거 문장 선택 |
| 5 | Rating Impact Analyzer | Feature × Journey 문제군의 prevalence, 부정 비율, rating drop 계산 |
| 6 | Improvement Recommendation | 담당 부서·실행 단계·KPI·제약을 포함한 개선조치 생성 |

Agent 1–4에는 Gold label이 아니라 리뷰 원문만 입력하고, Gold는 평가에만 사용했습니다. Agent 5는 LLM 판단이 아닌 재현 가능한 집계 코드이며, Agent 6와 RAG Judge는 구조화 출력 schema를 사용합니다.

## 직접 구현한 핵심 요소

- Sequential·Feedback·Orchestrator 구조를 동일 표본에서 비교하는 실험 설계
- 199개 고유 Gold 리뷰 기반 검증과 CLEAN_HOTEL 1,000개 확장 실행 구조
- `Feature × Customer Journey` 문제군별 부정 비율·prevalence·rating drop·우선순위 계산
- 한 행에 하나의 독립 조치를 저장하는 개선안 schema
- PDF·DOCX·TXT·MD·CSV·XLSX 문헌 ingestion과 embedding cache
- 문헌 상태 `SUPPORTED / CONTRADICTED / INSUFFICIENT_EVIDENCE` 분리
- Actionability, Specificity, Feasibility 등 8개 차원의 LLM-as-a-Judge
- JSONL 상태 파일 기반 재시작, execution log, handoff trace, fallback 기록

## 검증 기록

2026-08-02 패키지 검증에서는 다음 항목을 확인했습니다.

- Python 구문 검사 통과 및 자동 테스트 26개 통과
- API 없는 Pilot 20 준비 실행 통과, 리뷰 원문 20/20 존재
- Agent 1–4 예측 라벨 84개와 Agent 5 상위 문제군 5개 생성
- CLEAN_HOTEL 1,000 입력 로딩과 Agent 1–4 모의 실행 확인
- 결과 Excel 8종 생성·재로딩 확인

이 수치는 파이프라인 연결과 출력 구조 검증 결과입니다. Pilot 20은 통계적 일반화를 위한 최종 표본이 아니며, API key가 없던 검증 시점에는 Agent 6·문헌 embedding·RAG Judge의 실제 호출을 수행하지 않았습니다. 자세한 내용은 [`docs/VALIDATION_20260802.md`](docs/VALIDATION_20260802.md)에 기록했습니다.

## 공개 파일

```text
01-hotel-review-agentic-ai/
├── README.md
├── requirements.txt
├── src/
│   ├── hotel_agent56_pipeline.py   # Agent 5·6, RAG, Judge, 결과 저장
│   └── run_full1000_all.py         # Agent 1–4 이후 전체 실행 orchestrator
└── docs/
    ├── ORIGINAL_README_20260802.md
    └── VALIDATION_20260802.md
```

`hotel_agent56_pipeline.py`는 입력 병합, Pilot 선정, 별점 영향 분석, 개선안 생성, 문헌 청킹·검색, Judge, human evaluation template 및 Excel 결과 저장을 포함합니다.

## 실행 조건과 공개 범위

의존성은 다음 명령으로 설치할 수 있습니다.

```bash
python -m pip install -r requirements.txt
python src/hotel_agent56_pipeline.py --help
```

전체 실행에는 다음 비공개/제외 자료가 추가로 필요합니다.

- Gold·예측·CLEAN_HOTEL 입력 workbook
- Agent 1–4의 `legacy_agent1_4_v8_2` runner
- 검색 대상 문헌 폴더
- 실제 생성·평가 단계용 `OPENAI_API_KEY`

따라서 현재 공개 저장소는 코드 구조와 검증 기록을 확인하기 위한 포트폴리오 범위이며, clone 직후 end-to-end 재현 패키지는 아닙니다. 원래 패키지의 실행 방법과 결과 파일 정의는 [`docs/ORIGINAL_README_20260802.md`](docs/ORIGINAL_README_20260802.md)에 보존했습니다.

## 대표 원본

- [2026-08-18 연구 발표자료](https://docs.google.com/presentation/d/1Ed_i0fEzhS9CG1W-HtK3AdeAi0GueVdqgOOkaGfAUhQ/edit)
- [프로젝트 인수인계·면담 정리](https://docs.google.com/document/d/1784GDvROO9BrVhV52u9r0BNECQGdspFcVcnH5ag5EGE/edit)

Drive 링크는 공유 설정에 따라 별도 접근 권한이 필요할 수 있습니다.
