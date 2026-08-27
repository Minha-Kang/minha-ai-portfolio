# Google Drive 자료 선별·반입 인덱스

이 문서는 Google Drive에서 확인한 프로젝트 자료를 공개 GitHub 저장소에 실제 파일로 반입한 결과와 제외 기준을 기록합니다.

## 최종 프로젝트 구조

기존 5개 프로젝트를 다음 3개로 정리했습니다.

- 기존 Project 03 `Agent Execution Logging & Human Verification Pipeline` 제거
- 기존 Project 05 `XAI-Based UI Complexity Diagnostics`를 Project 04와 통합
- 통합 UI 프로젝트를 최종 Project 03으로 재번호화

| 최종 프로젝트 | Drive 관련 후보 | 새로 반입 | 저장소 최종 파일 수 |
|---|---:|---:|---:|
| 01. Hotel Review Agentic AI | 93 | 18 | 24 |
| 02. Multi-Agent Failure Attribution | 27 | 3 | 7 |
| 03. AndroidControl UI Readability & XAI | 35 | 5 | 6 |
| **합계** | **155** | **26** | **37** |

`Drive 관련 후보`는 인벤토리 단계에서 연결된 파일 수이며 중복·중간본을 포함합니다. `새로 반입`은 이번 정리에서 GitHub에 추가한 실제 Drive 파일 수입니다. `저장소 최종 파일 수`에는 기존 코드·CSV·README도 포함합니다.

## 선별 원칙

1. 최종 발표자료, 최종 보고서, 방법론, 검증 결과와 재현에 필요한 파일을 우선합니다.
2. 동일 내용의 여러 버전은 최신·최종본 한 개만 남깁니다.
3. 외부 benchmark의 원본 코드·논문 자산은 직접 구현한 것으로 오해되지 않도록 제외합니다.
4. API key, `.env`, cache, 전체 실행 log, 임시 파일과 대용량 raw dataset은 제외합니다.
5. 개인정보가 포함된 자료는 공개용 사본으로 정리하거나 제외합니다.

## Project 01 — Hotel Review Agentic AI

### 새로 반입한 18개 파일

| 구분 | 저장소 경로 |
|---|---|
| 연구 발표 | `projects/01-hotel-review-agentic-ai/docs/research/2026-08-18-research-presentation.pptx` |
| 인수인계·논문 초안 | `projects/01-hotel-review-agentic-ai/docs/research/research-handover-and-introduction.docx` |
| 방법론 | `docs/methodology/METHODOLOGY.md`, `AGENT_PIPELINE_OPTIMIZATION.md` |
| 구조 비교 | `docs/architecture/DYNAMIC_ORCHESTRATOR_V8.md`, `ARCHITECTURE_COMPARE_V6.md`, `ARCHITECTURE_PRECISION_V7.md` |
| 결과·감사 기록 | `docs/results/RESULTS.md`, `ZERO_COST_RESULTS.md`, `docs/validation/AGENT6_8258_AUDIT.md` |
| 데이터 split | `data/splits/architecture_sample_40_ids.txt`, `development_116_ids.txt`, `holdout_83_ids.txt` |
| 검증 workbook | `data/hotel_gold_label_200_guest_cycle_v8.xlsx`, `results/hotel_v8_199_regression_rag_judge.xlsx` |
| 운영 보고서 | `results/dynamic_orchestrator_manager_report.md`, `sequential_manager_report.md`, `pilot_summary_report.md` |

기존 GitHub의 코드 2개, `requirements.txt`, 원본 README와 validation 문서는 중복 반입하지 않고 그대로 유지했습니다.

### 제외

- 19,561개 전체 리뷰 모집단과 대용량 운영 입력
- 중간 실행 결과, cache, 전체 log, 이전 버전 workbook
- API key·환경설정과 별도 문헌 원문 폴더
- 동일 내용의 중복 발표·보고서

## Project 02 — Multi-Agent Failure Attribution

### 새로 반입한 3개 파일

- `docs/failure-attribution-analysis-report.docx`
- `docs/interim-presentation-query-task-agent.pptx`
- `docs/trajectory-quality-research-questions.pptx`

기존의 직접 작성한 요약 CSV 3종은 유지했습니다.

### 제외

- 외부 Who & When·Automated Failure Attribution 원본 코드와 논문 PDF
- 전체 trajectory 원본과 임시 EDA 산출물
- 중복 발표본과 수업 진행용 중간 파일

## Project 03 — AndroidControl UI Readability & XAI

### 새로 반입한 5개 파일

#### Agent 행동 기반 UI 가독성

- `behavior-analysis/docs/ui-readability-final-presentation.pptx`
- `behavior-analysis/docs/ui-readability-final-report.docx`
- `behavior-analysis/results/ui-readability-graph-appendix.pptx`

#### XAI 기반 UI 복잡도

- `xai/docs/xai-final-presentation-public.pdf`
- `xai/docs/xai-presentation-script.docx`

### 개인정보 처리

- XAI 원본 PDF 첫 페이지의 학번 5개와 팀원 이름을 제거했습니다.
- 마지막 기여 역할 표의 팀원 이름은 익명화하고, 강민하의 역할만 식별 가능한 형태로 유지했습니다.
- 개인정보가 포함된 원본 PDF는 GitHub에 포함하지 않았습니다.

### 제외

- AndroidControl raw dataset·screenshot·JSON 전체
- 중간 발표본, 중복 그래프와 중복 스크립트
- 학번·팀원 이름이 포함된 XAI 원본 PDF
- 외부 공개 dataset 자체와 학습 cache

## 공개 저장소 해석 기준

- 코드가 포함된 경우에도 제외된 입력 데이터·문헌·API 환경이 있으면 clone 직후 end-to-end 재현을 보장하지 않습니다.
- Excel 검증 자료에는 연구 과정에서 사용한 리뷰 문장과 평가 결과가 포함되어 있으므로, 2차 사용 전 원천 데이터의 이용 조건을 별도로 확인해야 합니다.
- 팀 프로젝트는 개인 기여 범위를 각 README에 구분해 적었으며, 팀 전체 결과를 개인 단독 구현으로 표현하지 않습니다.
