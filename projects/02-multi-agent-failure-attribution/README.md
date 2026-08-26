# Project 02. Who & When 기반 Multi-Agent 실패귀속 분석

멀티에이전트 시스템이 실패했을 때 **누가 실패했는지(Who)**와 **어느 단계가 결정적 오류인지(When)**를 분리해 분석한 벤치마크 EDA·연구질문 설계 프로젝트입니다.

## 문제 정의

최종 정답 여부만으로는 Planner, Searcher, Verifier, Orchestrator 중 어디서 문제가 시작됐는지 알기 어렵습니다. 이 프로젝트는 실패 책임 Agent와 결정적 오류 Step을 별도 대상으로 두고, trajectory를 Agent·Step 단위로 검토할 수 있는 분석 틀을 정리했습니다.

## 수행 범위

- Who & When benchmark와 Automated Failure Attribution 코드·데이터 구조 분석
- Algorithm-Generated와 Hand-Crafted split의 task·domain 구성 비교
- 14개 사례를 Retrieval Failure, Fabricated Evidence, Condition Omission, Tool Misuse, Verification Failure, Orchestrator Failure 등으로 재구성
- All-at-once, Step-by-step, Binary Search judge 방식의 평가 흐름 비교
- 조건 손실 탐지와 약한 성공 탐지로 후속 연구질문 확장

외부 benchmark의 원본 코드나 논문 자산은 직접 구현한 것으로 오해되지 않도록 저장소에서 제외하고, 직접 수행한 EDA 요약과 해석만 공개했습니다.

## 공개 데이터 요약

공개 CSV는 총 184개 task의 집계 결과입니다.

| 구분 | 개수 |
|---|---:|
| Algorithm-Generated | 126 |
| Hand-Crafted | 58 |
| 전체 | 184 |

가장 큰 coarse task group은 Documents / web / scholarly evidence 37개, Entertainment / media / arts 30개, Local travel / place finding 26개 순입니다.

## 관찰 결과

- 분석 당시 참고한 benchmark 결과에서 `Who ≈ 53.5%`, `When ≈ 14.2%`로, 책임 Agent보다 결정적 오류 Step 식별이 더 어려웠습니다.
- 동일한 최종 실패라도 검색 실패, 조건 누락, 검증 실패, orchestration 실패는 서로 다른 교정 전략이 필요했습니다.
- 최종 답이 맞더라도 중요한 조건을 잃어버린 **약한 성공**을 별도 탐지해야 trajectory 품질을 더 정확히 평가할 수 있다는 연구질문을 도출했습니다.

위 수치는 내가 새 모델을 학습해 달성한 성능이 아니라, benchmark·실험 결과를 분석한 관찰값입니다.

## 파일 안내

- [`data/overview_summary.csv`](data/overview_summary.csv): 8개 coarse task group별 전체 분포
- [`data/split_summary.csv`](data/split_summary.csv): Algorithm-Generated·Hand-Crafted split 비교
- [`data/detailed_summary.csv`](data/detailed_summary.csv): split별 세부 domain 분포
- [`DRIVE_PROJECT_README.md`](DRIVE_PROJECT_README.md): 원본 Drive 폴더 정리 기준

## 대표 원본

- [Who & When 분석보고서](https://docs.google.com/document/d/17boRWXEIRIYmRcNT9pFPKc5vWiwAuuU4/edit)
- [Query·Task·Agent 중간 분석 발표](https://docs.google.com/presentation/d/1aBjf0WK0DPluBDud9RzTWn8FR1iRtRMX/edit)
- [Trajectory Quality 최종 연구질문](https://docs.google.com/presentation/d/1n4HvSBqkAAN6EQguFYmFcV3I0_qddVwB/edit)

Drive 링크는 공유 설정에 따라 별도 접근 권한이 필요할 수 있습니다.
