# Project 01. Hotel Review Agentic AI

**Current research · Jun. 2026 - Present · Manuscript in preparation**

호텔 리뷰에서 서비스 경험의 근거를 찾고, 호텔별 개선 우선순위와 실행안까지 연결하는 LLM 기반 Agentic AI 연구입니다. 리뷰를 단순 분류하거나 요약하는 대신, 각 판단의 근거와 Agent 간 전달 과정을 남겨 결과를 다시 검토할 수 있게 설계했습니다.

## Research question

1. 리뷰에 나타난 서비스 경험은 어떤 Feature와 Customer Journey에 해당하는가?
2. 부정적 경험은 별점 하락과 어느 정도 관련되는가?
3. 호텔별로 어떤 문제를 먼저 개선해야 하는가?
4. 최종 개선안에서 원문 근거와 중간 판단을 다시 추적할 수 있는가?

## Pipeline

`Review body → Feature / Journey / Sentiment / Evidence → Rating impact → Hotel-level IPA/Q2 → Targeted actions`

- Agent 1-4: 리뷰 본문에서 서비스 경험과 근거를 구조화
- Agent 5: Feature·Journey별 부정 경험 비율과 별점 penalty 계산
- Deterministic IPA/Q2: 호텔별 개선 우선순위 선정
- Agent 6: 우선순위가 확인된 그룹에만 실행안 생성

Agent 1-4에는 리뷰 본문만 입력했습니다. 제목, 숫자 별점, Gold Feature·Journey·Sentiment·Evidence label은 평가와 후속 집계에만 사용했습니다.

## My role

연구 질문 설정, Agent workflow 설계, Gold-label 기준 작성과 수동 검수, 실행 코드, 평가, 오류 분석, 교수 면담 자료와 논문 초안 작성까지 전 과정을 맡아 진행하고 있습니다.

## Current dataset and output

| Item | Count |
|---|---:|
| Reviews (2023-2025) | 2,643 |
| Manually audited Gold reviews | 350 |
| Gold service mentions | 1,438 |
| Gold Feature × Journey labels | 1,298 |
| Agent 1-4 output labels | 8,085 |
| Rating-impact records | 2,369 |
| Hotels included in IPA/Q2 | 14 |
| Priority Features | 27 |
| Observed Feature × Journey groups | 47 |
| Final actions | 94 |

## Gold 350 evaluation

| Unit | Precision | Recall | F1 |
|---|---:|---:|---:|
| Feature | 0.904 | 0.733 | 0.809 |
| Journey | 0.864 | 0.788 | 0.824 |
| Feature × Journey | 0.778 | 0.632 | 0.697 |

- Sentiment direction accuracy: 91.18%
- Predicted evidence found in the review body: 98.67%
- Gold evidence match within matched Feature × Journey cases: 91.05%

이 수치는 현재 Gold 350 기준 중간 결과입니다. 원인 분석과 규칙 수정이 끝난 뒤 동일 기준으로 다시 평가할 예정입니다.

## What the error analysis changed

Journey label이 J00에 과도하게 모이는 현상을 확인했습니다. 또한 475개의 Feature × Journey false negative 중 56개는 중간 Agent에서 찾았지만 precision guardrail을 통과하지 못해 제거됐습니다.

현재는 J00/J01/J02/J04 구분과 evidence 조건을 수정하고 있습니다. Gold 350에서 개선이 확인된 경우에만 2,643개 전체를 다시 실행합니다. 이 순서를 둔 이유는 전체 실행 결과를 먼저 만든 뒤 평가 기준을 맞추는 일을 피하기 위해서입니다.

## Reproducibility

- Fixed model snapshot and review-body-only input
- Data hash, model, prompt and code version checks
- Parallel workers and resumable checkpoints
- Selective Agent 6 execution for observed priority groups
- Retry for transient network errors; stop on auth, quota, schema or hash mismatch
- Execution log, handoff trace, fallback record and source-level audit chain

## Repository contents

### Code

- [Agent 5·6 and result pipeline](src/hotel_agent56_pipeline.py)
- [Full-sample execution orchestrator](src/run_full1000_all.py)
- [Python requirements](requirements.txt)

### Research notes and earlier experiments

- [2026-08-18 research presentation](docs/research/2026-08-18-research-presentation.pptx)
- [Research handover and Introduction draft](docs/research/research-handover-and-introduction.docx)
- [Methodology](docs/methodology/METHODOLOGY.md)
- [Pipeline optimization notes](docs/methodology/AGENT_PIPELINE_OPTIMIZATION.md)
- [Architecture comparison documents](docs/architecture/)

### Validation and results

- [Gold 200 workbook from the earlier validation stage](data/hotel_gold_label_200_guest_cycle_v8.xlsx)
- [Gold 199 regression and RAG Judge workbook from the earlier stage](results/hotel_v8_199_regression_rag_judge.xlsx)
- [Manager reports](results/)
- [Result notes](docs/results/)
- [Agent 6 audit](docs/validation/AGENT6_8258_AUDIT.md)

일부 공개 파일은 Gold 199/200 및 1,000개 실행 단계의 기록입니다. 위 README의 Gold 350·2,643개 수치는 이후 진행된 현재 연구 상태이며, 최신 검증 파일은 연구가 진행 중이므로 아직 공개하지 않았습니다.

Raw review population, API credentials, cache, full execution logs and duplicate intermediate files are excluded. The rating-impact score is an observational priority measure, not a causal estimate of the effect of service improvement.

