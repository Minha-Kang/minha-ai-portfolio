# 강민하 — AI·데이터 분석 프로젝트 포트폴리오

아주대학교 산업공학과에서 수행한 **Agentic AI, LLM 평가, 텍스트 마이닝, 서비스공학, 머신러닝 프로젝트**를 문제 정의·담당 범위·분석 방법·검증 근거가 드러나도록 정리한 저장소입니다.

최종 결과만 나열하기보다 “어떤 문제를 풀었는지, 무엇을 직접 구현하거나 분석했는지, 현재 공개 자료만으로 어디까지 확인할 수 있는지”를 프로젝트별 README에 구분해 기록했습니다.

## 관심 분야

- Agentic AI workflow 설계와 구조 비교
- LLM 응답 품질 평가, LLM-as-a-Judge, failure attribution
- 자연어 리뷰 마이닝과 서비스 품질 분석
- 실행 로그, audit trail, fallback 기반 AI 신뢰성 검증
- 데이터 기반 서비스 개선과 산업공학 응용

## 프로젝트 한눈에 보기

총 8개 프로젝트를 8개 주제 폴더에 정리했습니다. 구현·연구, 벤치마크 분석, 실행 로그 검증, 서비스 설계, 머신러닝 실습, 산업공학 분석을 프로젝트별로 구분했습니다.

| 번호 | 프로젝트 | 수행 형태 | 핵심 작업 | 저장소에서 확인 가능한 자료 |
|---:|---|---|---|---|
| 01 | [호텔 리뷰 Agentic AI 서비스 품질평가](projects/01-hotel-review-agentic-ai/) | 구현·연구 | 6단계 분석, 별점 영향 계산, 개선안 생성, Literature RAG Judge | Python 2개, 요구사항, 검증 문서 |
| 02 | [Who & When 기반 Multi-Agent 실패귀속](projects/02-multi-agent-failure-attribution/) | 벤치마크 분석·EDA | 실패 Agent와 결정적 오류 Step 분리, failure taxonomy 재구성 | 184개 task의 요약 CSV 3종 |
| 03 | [Agent Trajectory Log 실행·수동검증](projects/03-agent-trajectory-validation/) | 파이프라인 설계·실행 | Step log, task summary, human review template | 실행 요약 샘플·설정·검수 양식 |
| 04 | [AndroidControl 기반 UI 가독성 분석](projects/04-androidcontrol-ui-readability/) | EDA·연구 설계 | 데이터 정제, 행동 분포·entropy 기반 UI 특성 설계 | 분석 요약·발표/보고서 링크 |
| 05 | [XAI 기반 쇼핑 앱 UI 복잡도 진단](projects/05-xai-shopping-ui-complexity/) | 팀 프로젝트 | UI 복잡도 특성화, 설명 가능한 개선 방향 도출 | 역할·방법 요약·발표 링크 |
| 06 | [Ajou Career Navigator](projects/06-ajou-career-navigator/) | 서비스 설계 | 취업 준비 행동 기반 학생 세분화와 개인화 설계 | 분석 계획·서비스 구조·보고서 링크 |
| 07 | [MNIST·KOSPI 딥러닝 실습](projects/07-ml-mini-projects/) | 개인 실습 | FCN/CNN 이미지 분류, RNN 시계열 예측 | 데이터·모델·실행 결과 요약 |
| 08 | [신뢰성·인간공학 분석](projects/08-industrial-engineering-analysis/) | 산업공학 프로젝트 | 반복 굽힘 수명과 작업환경 문제 분석 | 수행 내용·보고서 링크 |

## 대표 역량

### 1. AI 출력을 다시 검증할 수 있는 구조로 전환

호텔 리뷰 프로젝트에서는 최종 응답만 저장하지 않고 판단 근거, Agent handoff, fallback event, metric formula, 실행 로그와 관리자용 개선안을 분리했습니다. 이를 통해 결과가 생성된 과정을 사람과 코드가 다시 확인할 수 있도록 설계했습니다.

### 2. Agent 실패를 Agent·Step 단위로 분석

Who & When 벤치마크의 184개 task를 분석해 실패 책임 Agent와 결정적 오류 Step을 구분했습니다. 공개 요약 데이터는 Algorithm-Generated 126개, Hand-Crafted 58개로 구성되며, 후속 연구 질문을 조건 손실과 약한 성공 탐지로 확장했습니다.

### 3. 모델 결과를 서비스 개선안으로 연결

리뷰의 Feature·Customer Journey·Sentiment를 별점 하락과 연결하고, 담당 부서·실행 단계·KPI·제약조건을 갖춘 개선조치 schema로 변환했습니다. Ajou Career Navigator에서는 분석 기법을 학생 세분화와 상담·프로그램 추천 구조로 연결했습니다.

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
│   ├── 05-xai-shopping-ui-complexity/
│   ├── 06-ajou-career-navigator/
│   ├── 07-ml-mini-projects/
│   └── 08-industrial-engineering-analysis/
└── docs/
    └── DRIVE_SOURCE_INDEX.md
```

## 공개 범위와 재현성

- 최신 대표본과 직접 작성한 코드·분석 요약을 우선했습니다.
- API key, `.env`, 개인정보, 캐시, 대용량 원본 데이터는 포함하지 않습니다.
- 외부 benchmark의 원본 코드와 자료는 내 구현으로 오해되지 않도록 제외했습니다.
- 코드가 없는 프로젝트는 **분석/설계 포트폴리오**, 코드가 있는 Project 01은 **공개 코드 + 검증 기록**으로 구분했습니다.
- Project 01의 전체 재실행에는 공개 저장소에 없는 입력 workbook, 문헌, Agent 1–4 legacy runner가 추가로 필요합니다. 공개 코드만으로는 구문과 구현 구조를 확인할 수 있습니다.
- Drive 링크는 원본 자료의 위치를 기록한 것이며, 파일별 공유 설정에 따라 별도 접근 권한이 필요할 수 있습니다.

자료 선별 기준은 [Drive 자료 인덱스](docs/DRIVE_SOURCE_INDEX.md)에서 확인할 수 있습니다.
