# Project 02. Multi-Agent Failure Attribution & Trajectory Quality

**Completed · Apr. - Jun. 2026**

멀티에이전트 시스템의 실패를 최종 정답 여부만으로 보지 않고, 책임 Agent(Who)와 결정적 오류 Step(When)으로 나누어 분석한 프로젝트입니다. Who&When benchmark의 저자나 원 연구 참여자가 아니라, 공개 benchmark를 독립적으로 재현하고 분석했습니다.

## What I did

- 127개 multi-agent system에서 수집된 184개 failure-attribution task 분석
- All-at-Once, Step-by-Step, Binary Search baseline 재현
- 논문의 방법론, prompt template, repository implementation, evaluator logic과 split schema 감사
- Algorithm-Generated 126개와 Hand-Crafted 58개 split의 task·domain·trajectory 길이 비교
- 최종 성공 여부를 넘어 Condition Loss와 Weak Success를 보는 후속 연구질문 설계

## Why step-level attribution is difficult

분석 대상 benchmark에서 보고된 최고 성능은 Who 약 53.5%, When 약 14.2%였습니다. 이 값은 제가 새 모델을 학습해 달성한 성능이 아니라 원 benchmark의 결과입니다. 책임 Agent를 고르는 것보다 긴 trajectory 안에서 결정적 오류 Step을 특정하는 일이 훨씬 어렵다는 점을 보여줍니다.

Hand-Crafted split의 mistake step은 평균 15.16, 최대 82였고, 전체 trace는 최대 130 step까지 이어졌습니다.

## Audit findings

- 기본 prompt에 ground truth가 포함되어 있어 실제 `without ground truth` 조건에는 코드 수정이 필요했습니다.
- split에 따라 Agent를 `name` 또는 `role`로 기록해 evaluator matching 오류 가능성이 있었습니다.
- Binary Search evaluator가 모호하게 답할 때 분기 방향이 무작위로 정해질 수 있었습니다.
- evaluator-agent matching이 exact match가 아닌 substring 기준이었습니다.

이 문제들은 방법 간 성능 차이를 해석하기 전에 평가 파이프라인 자체를 먼저 확인해야 한다는 근거가 됐습니다.

## Exploratory extension

- **Condition Loss**: task의 중요한 조건이 active trajectory에서 처음 사라지는 시점은 언제인가?
- **Weak Success**: 최종 답은 맞지만 중간 과정이 취약한 사례를 구분할 수 있는가?

두 항목은 완료된 benchmark 분석에서 도출한 연구 아이디어이며, 별도의 완성 모델 성능으로 제시하지 않습니다.

## Files

- [Failure attribution analysis report](docs/failure-attribution-analysis-report.docx)
- [Query·Task·Agent interim presentation](docs/interim-presentation-query-task-agent.pptx)
- [Trajectory quality research questions](docs/trajectory-quality-research-questions.pptx)
- [Coarse task group summary](data/overview_summary.csv)
- [Split summary](data/split_summary.csv)
- [Detailed domain summary](data/detailed_summary.csv)

원 benchmark의 코드, 논문 PDF와 전체 trajectory는 직접 만든 자료로 오해되지 않도록 포함하지 않았습니다.

