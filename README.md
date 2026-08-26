# 강민하 — AI·데이터 분석 프로젝트 포트폴리오

아주대학교 산업공학과에서 수행한 Agentic AI, LLM 평가, 텍스트 마이닝, 서비스공학, 머신러닝 프로젝트를 문제 정의·담당 범위·분석 방법·검증 근거가 드러나도록 정리한 저장소입니다.

최종 결과만 나열하기보다 “어떤 문제를 풀었는지, 무엇을 직접 구현하거나 분석했는지, 현재 공개 자료만으로 어디까지 확인할 수 있는지”를 프로젝트별 README에 구분해 기록했습니다.

## 관심 분야

- Agentic AI workflow 설계와 구조 비교
- LLM 응답 품질 평가, LLM-as-a-Judge, failure attribution
- 자연어 리뷰 마이닝과 서비스 품질 분석
- 실행 로그, audit trail, fallback 기반 AI 신뢰성 검증
- 데이터 기반 서비스 개선과 산업공학 응용

## 프로젝트 한눈에 보기

총 5개 핵심 프로젝트를 5개 주제 폴더에 정리했습니다. Agentic AI 구현·연구, 벤치마크 분석, 실행 로그 검증, UI 행동 분석과 XAI 모델링을 프로젝트별로 구분했습니다.

| 번호 | 프로젝트 | 수행 형태 | 핵심 작업 | 저장소에서 확인 가능한 자료 |
|---:|---|---|---|---|
| 01 | [LLM-Based Multi-Agent Service Quality Evaluation from Hotel Reviews](projects/01-hotel-review-agentic-ai/) | 구현·연구 | 6단계 분석, 별점 영향 계산, 개선안 생성, Literature RAG Judge | Python 2개, 요구사항, 검증 문서 |
| 02 | [Multi-Agent Failure Attribution & Trajectory Quality](projects/02-multi-agent-failure-attribution/) | 벤치마크 분석·EDA | 실패 Agent와 결정적 오류 Step 분리, failure taxonomy 재구성 | 184개 task의 요약 CSV 3종 |
| 03 | [Agent Execution Logging & Human Verification Pipeline](projects/03-agent-trajectory-validation/) | 파이프라인 설계·실행 | Step log, task summary, human review template | 실행 요약 샘플·설정·검수 양식 |
| 04 | [Agent Behavior–Based UI Readability Analysis with AndroidControl](projects/04-androidcontrol-ui-readability/) | EDA·연구 설계 | 데이터 정제, 행동 분포·entropy 기반 UI 특성 설계 | 분석 요약·발표/보고서 링크 |
| 05 | [XAI-Based UI Complexity Diagnostics with AndroidControl](projects/05-xai-shopping-ui-complexity/) | 팀 프로젝트 | UI 복잡도 특성화, 설명 가능한 개선 방향 도출 | 역할·방법 요약·발표 링크 |

## 대표 역량

### 1. AI 출력을 다시 검증할 수 있는 구조로 전환

호텔 리뷰 프로젝트에서는 최종 응답만 저장하지 않고 판단 근거, Agent handoff, fallback event, metric formula, 실행 로그와 관리자용 개선안을 분리했습니다. 이를 통해 결과가 생성된 과정을 사람과 코드가 다시 확인할 수 있도록 설계했습니다.

### 2. Agent 실패를 Agent·Step 단위로 분석

Who & When 벤치마크의 184개 task를 분석해 실패 책임 Agent와 결정적 오류 Step을 구분했습니다. 공개 요약 데이터는 Algorithm-Generated 126개, Hand-Crafted 58개로 구성되며, 후속 연구 질문을 조건 손실과 약한 성공 탐지로 확장했습니다.

### 3. 모델 결과를 서비스 개선안으로 연결

리뷰의 Feature·Customer Journey·Sentiment를 별점 하락과 연결하고, 담당 부서·실행 단계·KPI·제약조건을 갖춘 개선조치 schema로 변환했습니다.

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


