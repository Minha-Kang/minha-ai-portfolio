# 강민하 — AI·데이터 분석 프로젝트 포트폴리오

아주대학교 산업공학과에서 Agentic AI, LLM 평가, 텍스트 마이닝과 서비스공학을 중심으로 연구·프로젝트를 수행해 왔습니다.

현재는 **호텔 리뷰를 여러 AI Agent가 단계별로 분석하고, 호텔별 서비스 개선 우선순위와 실행안을 도출하는 연구를 논문으로 작성하고 있습니다.** 이 저장소는 해당 연구를 대표 프로젝트로 두고, Multi-Agent 실패 분석과 AndroidControl 기반 UI 분석 경험을 함께 정리했습니다.

결과만 요약하지 않고 직접 작성한 코드, 검증 결과, 발표자료와 보고서를 저장소 안에서 바로 확인할 수 있도록 구성했습니다.

## 관심 분야

- Agentic AI workflow 설계와 Single LLM·Multi-Agent 구조 비교
- LLM 응답 품질 평가, LLM-as-a-Judge와 failure attribution
- 호텔 리뷰 마이닝과 서비스 품질 개선 우선순위 분석
- 실행 로그·audit trail 기반 AI 신뢰성 검증
- Agent 행동과 XAI를 활용한 UI 복잡도 진단

## 프로젝트 한눈에 보기

| 번호 | 프로젝트 | 수행 형태 | 핵심 내용 | 저장소 자료 |
|---:|---|---|---|---|
| 01 | [LLM-Based Multi-Agent Service Quality Evaluation from Hotel Reviews](projects/01-hotel-review-agentic-ai/) | **대표 연구·논문 작성 중** | 6-Agent 분석, 별점 영향, 호텔별 IPA, 운영 개선안, Literature RAG Judge | 코드·연구 발표·방법론·검증 workbook·관리자 보고서 |
| 02 | [Multi-Agent Failure Attribution & Trajectory Quality](projects/02-multi-agent-failure-attribution/) | 벤치마크 분석·EDA | 실패 Agent와 결정적 오류 Step 분리, failure taxonomy와 후속 연구질문 설계 | 분석보고서·발표자료 2종·요약 CSV 3종 |
| 03 | [AndroidControl UI Readability & XAI Complexity Analysis](projects/03-androidcontrol-ui-analysis/) | EDA·연구 설계·팀 프로젝트 | Agent 행동 기반 UI 가독성과 XAI 기반 쇼핑 UI 복잡도 분석을 하나의 프로젝트로 통합 | 최종 보고서·발표자료·그래프 부록·공개용 XAI 발표자료·스크립트 |

## 대표 역량

### 1. AI의 판단 과정을 다시 확인할 수 있도록 설계

호텔 리뷰 연구에서는 최종 답변만 저장하지 않고 판단 근거, Agent 간 전달 과정, 실행 로그, fallback event와 계산 결과를 구분했습니다. 이를 통해 결과가 어떻게 만들어졌는지 다시 확인하고 오류가 시작된 단계를 추적할 수 있도록 설계했습니다.

### 2. Agent 실패를 Agent·Step 단위로 분석

Who & When 벤치마크의 184개 task를 분석해 실패 책임 Agent와 결정적 오류 Step을 구분했습니다. 분석 결과를 조건 손실과 약한 성공 탐지라는 후속 연구질문으로 확장했습니다.

### 3. 분석 결과를 실제 개선 문제로 연결

호텔 리뷰에서는 Feature·Customer Journey·Sentiment를 별점 하락과 개선 우선순위로 연결했습니다. UI 프로젝트에서는 화면 자체의 특성뿐 아니라 Agent 행동 분포와 XAI 결과를 이용해 사람이 검토할 수 있는 개선 방향을 제안했습니다.

## 저장소 구조

```text
minha-ai-portfolio/
├── README.md
├── profile/
│   └── PROFILE.md
├── projects/
│   ├── 01-hotel-review-agentic-ai/
│   ├── 02-multi-agent-failure-attribution/
│   └── 03-androidcontrol-ui-analysis/
└── docs/
    └── DRIVE_SOURCE_INDEX.md
```

Drive에서 선별해 반입한 파일과 제외 기준은 [자료 선별·반입 인덱스](docs/DRIVE_SOURCE_INDEX.md)에 기록했습니다.
