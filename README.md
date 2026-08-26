# 강민하 — AI·데이터 분석 프로젝트 포트폴리오

아주대학교 산업공학과에서 Agentic AI, LLM 평가, 텍스트 마이닝과 서비스공학을 중심으로 프로젝트를 수행해 왔습니다.

특히 현재는 **호텔 리뷰를 여러 AI Agent가 단계별로 분석하고, 호텔별 서비스 개선 우선순위와 실행안을 도출하는 연구를 논문으로 작성하고 있습니다.** 이 저장소에는 해당 연구를 중심으로, 지금까지 진행한 Multi-Agent 평가·실행 로그 검증·UI 분석 프로젝트를 함께 정리했습니다.

## 관심 분야

- Agentic AI workflow 설계와 구조 비교
- LLM 응답 품질 평가와 LLM-as-a-Judge
- 호텔 리뷰 마이닝과 서비스 품질 분석
- Agent 실행 로그와 failure attribution
- 분석 결과를 실제 서비스 개선안으로 연결하는 방법

## 프로젝트 한눈에 보기

총 5개의 핵심 프로젝트를 정리했습니다. 각 프로젝트의 문제 정의와 수행 내용, 분석 방법, 검증 자료는 개별 README에서 자세히 확인할 수 있습니다.

| 번호 | 프로젝트 | 수행 형태 | 핵심 작업 | 저장소 자료 |
|---:|---|---|---|---|
| 01 | [LLM-Based Multi-Agent Service Quality Evaluation from Hotel Reviews](projects/01-hotel-review-agentic-ai/) | **대표 연구·논문 작성 중** | 6-Agent 리뷰 분석, 별점 영향 계산, 호텔별 개선 우선순위와 실행안 생성, Literature RAG Judge | Python 코드, 요구사항, 검증 문서 |
| 02 | [Multi-Agent Failure Attribution & Trajectory Quality](projects/02-multi-agent-failure-attribution/) | 벤치마크 분석·EDA | 실패한 Agent와 결정적 오류 Step 분리, failure taxonomy 재구성 | 184개 task의 요약 CSV 3종 |
| 03 | [Agent Execution Logging & Human Verification Pipeline](projects/03-agent-trajectory-validation/) | 파이프라인 설계·실행 | Step log, task summary, human review template 구성 | 실행 요약 샘플, 설정, 검수 양식 |
| 04 | [Agent Behavior–Based UI Readability Analysis with AndroidControl](projects/04-androidcontrol-ui-readability/) | EDA·연구 설계 | 데이터 정제, 행동 분포와 entropy 기반 UI 특성 설계 | 분석 요약, 발표·보고서 링크 |
| 05 | [XAI-Based UI Complexity Diagnostics with AndroidControl](projects/05-xai-shopping-ui-complexity/) | 팀 프로젝트 | UI 복잡도 특성화와 설명 가능한 개선 방향 도출 | 역할·방법 요약, 발표자료 링크 |

## 대표 역량

### 1. AI의 판단 과정을 다시 확인할 수 있도록 설계

호텔 리뷰 연구에서는 최종 답변만 저장하지 않고, 판단 근거와 Agent 간 전달 과정, 실행 로그, fallback event와 계산 결과를 구분해 기록했습니다. 이를 통해 결과가 어떻게 만들어졌는지 다시 확인하고, 문제가 발생한 단계를 추적할 수 있도록 설계했습니다.

### 2. Agent 실패를 Agent·Step 단위로 분석

Who & When 벤치마크의 184개 task를 분석해 실패 책임 Agent와 결정적 오류 Step을 구분했습니다. 공개 데이터는 Algorithm-Generated 126개와 Hand-Crafted 58개로 구성되며, 분석 결과를 조건 손실과 약한 성공 탐지라는 후속 연구 질문으로 확장했습니다.

### 3. 분석 결과를 실제 개선안으로 연결

호텔 리뷰에서 추출한 Feature·Customer Journey·Sentiment를 별점 하락과 연결하고, 담당 부서·실행 단계·KPI·제약조건을 포함한 개선안으로 변환했습니다. 단순히 리뷰를 분류하는 데서 끝나지 않고, 호텔 담당자가 어떤 문제를 먼저 개선해야 하는지 판단할 수 있는 구조를 만드는 데 초점을 두었습니다.

## 저장소 구조

```text
minha-ai-portfolio/
├── README.md
├── profile/
│   └── PROFILE.md
├── projects/
│   ├── 01-hotel-review-agentic-ai/
│   ├── 02-multi-agent-failure-attribution/
│   ├── 03-agent-trajectory-validation/
│   ├── 04-androidcontrol-ui-readability/
│   └── 05-xai-shopping-ui-complexity/
└── docs/
    └── DRIVE_SOURCE_INDEX.md
```
