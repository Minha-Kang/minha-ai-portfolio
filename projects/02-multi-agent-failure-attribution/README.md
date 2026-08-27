# Project 02. Multi-Agent Failure Attribution & Trajectory Quality

*Who & When 벤치마크 기반 멀티에이전트 실패귀속 및 궤적 품질 분석*

멀티에이전트 시스템이 실패했을 때 누가 실패했는지(Who)와 어느 단계가 결정적 오류인지(When)를 분리해 분석한 벤치마크 EDA·연구질문 설계 프로젝트입니다.

## 문제 정의

최종 정답 여부만으로는 Planner, Searcher, Verifier, Orchestrator 중 어디에서 문제가 시작됐는지 알기 어렵습니다. 이 프로젝트는 실패 책임 Agent와 결정적 오류 Step을 별도 대상으로 두고, trajectory를 Agent·Step 단위로 검토하는 분석 틀을 정리했습니다.

## 수행 범위

- Who & When benchmark와 Automated Failure Attribution의 코드·데이터 구조 분석
- Algorithm-Generated와 Hand-Crafted split의 task·domain 구성 비교
- 14개 사례를 Retrieval Failure, Fabricated Evidence, Condition Omission, Tool Misuse, Verification Failure, Orchestrator Failure 등으로 재구성
- All-at-once, Step-by-step, Binary Search judge 방식의 평가 흐름 비교
- 조건 손실 탐지와 약한 성공 탐지로 후속 연구질문 확장

외부 benchmark의 원본 코드와 논문 자산은 직접 구현한 것으로 오해되지 않도록 제외하고, 직접 수행한 분석·해석과 발표 산출물만 공개했습니다.

## 공개 데이터 요약

| 구분 | 개수 |
|---|---:|
| Algorithm-Generated | 126 |
| Hand-Crafted | 58 |
| 전체 | 184 |

가장 큰 coarse task group은 Documents / web / scholarly evidence 37개, Entertainment / media / arts 30개, Local travel / place finding 26개 순입니다.

## 관찰 결과

- 분석 당시 참고한 benchmark 결과에서 `Who ≈ 53.5%`, `When ≈ 14.2%`로, 책임 Agent보다 결정적 오류 Step 식별이 더 어려웠습니다.
- 같은 최종 실패라도 검색 실패, 조건 누락, 검증 실패와 orchestration 실패는 서로 다른 교정 전략이 필요했습니다.
- 최종 답이 맞더라도 중요한 조건을 잃어버린 약한 성공을 별도로 탐지해야 trajectory 품질을 더 정확히 평가할 수 있다는 연구질문을 도출했습니다.

위 수치는 새 모델을 학습해 달성한 성능이 아니라 benchmark·실험 결과를 분석한 관찰값입니다.

## 저장소에서 확인할 수 있는 자료

### 분석 문서

- [Who & When 분석보고서](docs/failure-attribution-analysis-report.docx)
- [Query·Task·Agent 중간 분석 발표](docs/interim-presentation-query-task-agent.pptx)
- [Trajectory Quality 최종 연구질문](docs/trajectory-quality-research-questions.pptx)

### 요약 데이터

- [8개 coarse task group 분포](data/overview_summary.csv)
- [Algorithm-Generated·Hand-Crafted split 비교](data/split_summary.csv)
- [split별 세부 domain 분포](data/detailed_summary.csv)

## 파일 구성

```text
02-multi-agent-failure-attribution/
├── README.md
├── docs/
│   ├── failure-attribution-analysis-report.docx
│   ├── interim-presentation-query-task-agent.pptx
│   └── trajectory-quality-research-questions.pptx
└── data/
    ├── overview_summary.csv
    ├── split_summary.csv
    └── detailed_summary.csv
```

이 폴더에는 README를 포함해 7개 파일이 있습니다. 원본 benchmark 코드·논문 PDF·전체 trajectory와 중복 발표본은 포함하지 않았습니다. 선별 근거는 [Drive 자료 선별 인덱스](../../docs/DRIVE_SOURCE_INDEX.md)에 기록했습니다.
