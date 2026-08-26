# Project 03. Agent Trajectory Log 실행·수동검증 파이프라인

Agent 실행 결과를 최종 답변만으로 평가하지 않고, task별 step log와 summary로 저장해 사람이 다시 검토할 수 있도록 만든 실행·평가 파이프라인 프로젝트입니다.

## 문제 정의

Agent가 틀린 답을 냈을 때 최종 응답만 남아 있으면 어떤 단계에서 문제가 시작됐는지 확인하기 어렵습니다. Planner·Searcher·Verifier·Answerer의 행동을 분리해 기록하고, 자동 지표와 수동 검수를 함께 사용할 수 있는 최소 평가 데이터 구조를 설계했습니다.

## 구현한 workflow

1. Planner가 task 해결 계획 생성
2. Searcher가 필요한 정보 탐색
3. Verifier가 근거와 조건 충족 여부 확인
4. Answerer가 최종 답변 작성
5. task별 latency·step 수·Verifier 결과 요약
6. Agent별 적절성을 사람이 표시하는 review template 생성

소규모 실행을 batch 실행으로 확장하면서 진행 상태, 모델, 저장 주기와 실행 폴더를 config로 남기도록 구성했습니다.

## 공개 샘플

공개 저장소에는 전체 실행 데이터 대신 5개 task의 결과 샘플과 100-task batch 설정을 포함했습니다.

| 파일 | 내용 |
|---|---|
| [`data/task_summary.csv`](data/task_summary.csv) | run/task ID, query, model, step 수, latency, 최종 답변 |
| [`data/manual_review_template.csv`](data/manual_review_template.csv) | Planner·Searcher·Verifier·Answerer의 수동 적절성 label |
| [`data/run_config.json`](data/run_config.json) | 모델, task 수, 저장 주기, 실행 목표 |

CSV의 열차 시각과 경로 답변은 당시 파이프라인 실행을 보여주는 **평가용 기록**이며, 현재 운행 정보를 제공하는 데이터가 아닙니다.

## 활용 의미

- 실패가 시작된 Agent와 Step을 사람이 역추적할 수 있습니다.
- 동일 task에 대한 LLM Judge label과 human label을 비교할 수 있습니다.
- latency·step 수·검증 결과를 task 단위 분석표로 확장할 수 있습니다.
- Project 02의 Who/When failure attribution 연구를 실행 로그 관점에서 연결할 수 있습니다.

## 공개 범위

현재 저장소에는 원본 runner와 전체 step-level log가 아니라 대표 요약·설정·검수 양식만 포함되어 있습니다. 따라서 실행 코드 재현보다는 평가 데이터 schema와 검수 workflow를 보여주는 포트폴리오 자료입니다. 원본 폴더 구성은 [`DRIVE_PROJECT_README.md`](DRIVE_PROJECT_README.md)에 기록했습니다.
