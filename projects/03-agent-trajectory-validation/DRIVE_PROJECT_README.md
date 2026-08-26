# Project 03. Agent Trajectory Log 실행 및 수동검증 파이프라인

## 개요
Agent 실행 과정을 step 단위로 기록하고, summary와 manual check template로 검증 가능하게 만든 프로젝트입니다.

## 폴더 구성
- 00_original_AgentAI_Trajectory_Logs: AgentAI_Trajectory_Logs 원본 폴더 전체입니다.
- 01_original_outputs: outputs 원본 폴더 전체입니다.
- 02_portfolio_named_key_files: 실행 로그, step 기록, summary, manual check template, batch run 시각화 파일을 한글 설명 파일명으로 정리했습니다.

## 설명 문장
본 프로젝트에서는 agent 실행 결과를 단순 최종 결과가 아니라 step-level log와 summary로 저장했습니다.
이를 통해 어떤 task에서 어떤 step이 실행되었는지 추적할 수 있고, manual check template를 통해 사람이 직접 검증할 수 있는 구조를 만들었습니다.

