# 강민하 | AI·데이터 분석 포트폴리오

아주대학교 산업공학과에서 텍스트 마이닝, LLM 기반 Agent 시스템, AI 평가와 서비스 분석을 공부하고 있습니다. 데이터를 분석하는 데서 그치지 않고, 결과가 어떤 근거와 과정을 거쳐 나왔는지 확인할 수 있는 시스템을 만드는 데 관심이 있습니다.

현재 SI.lab에서 호텔 리뷰를 서비스 개선 우선순위와 실행안으로 연결하는 Agentic AI 연구를 진행하고 있습니다. 나머지 세 프로젝트는 수업 및 연구 활동에서 완료한 작업입니다.

## Projects

| No. | Project | Status | What I worked on |
|---:|---|---|---|
| 01 | [Hotel Review Agentic AI](projects/01-hotel-review-agentic-ai/) | **Current research** | 2,643개 호텔 리뷰, Gold 350 수동 검수, 6-Agent 분석, 호텔별 IPA/Q2와 개선안 도출 |
| 02 | [Multi-Agent Failure Attribution](projects/02-multi-agent-failure-attribution/) | Completed | Who&When benchmark 재현, prompt·repository·evaluator 감사, trajectory 단위 오류 분석 |
| 03 | [AndroidControl UI Behavior & XAI](projects/03-androidcontrol-ui-analysis/) | Completed | Agent 행동 데이터 구조화와 UI 가독성 분석, 팀 XAI 프로젝트의 데이터 전처리·보고서 작성 |
| 04 | [Time-Use-Based B2B Service Recommendation](projects/04-time-use-b2b-service-recommendation/) | Completed | 생활시간조사 28개 변수를 8개 생활지수로 구성하고 Entropy-ROC·QFD로 6개 서비스 모듈 추천 |

## Current research

Project 01은 호텔 리뷰 전체 문장을 입력으로 받아 Feature, Customer Journey, Sentiment, Evidence를 추출하고, 그 결과를 별점 영향과 호텔별 개선 우선순위로 연결하는 연구입니다.

- 분석 대상: 2023-2025년 리뷰 2,643개
- 검증 기준: Gold 350개 리뷰를 직접 수동 검수
- 현재 결과: Agent 1-4 label 8,085개, impact record 2,369개, 14개 호텔의 우선 개선 Feature 27개, 최종 action 94개
- 현재 작업: J00 쏠림과 evidence guardrail로 인한 누락을 Gold 350에서 다시 점검한 뒤 전체 재실행 여부 결정

Agent 1-4에는 리뷰 본문만 제공하고 제목, 별점, Gold label은 제공하지 않았습니다. 분석 단계의 출력, handoff, 실행 로그와 fallback을 따로 남겨 오류가 어디서 시작됐는지 확인할 수 있게 구성했습니다.

## What I focus on

- Text mining and review analytics
- LLM-based multi-agent workflow design
- Gold-label validation and failure analysis
- Service analytics and decision support
- Reproducible data and evaluation pipelines

## Repository guide

각 프로젝트 폴더에는 문제 정의, 수행 범위, 주요 결과, 개인 기여와 공개 가능한 산출물을 정리했습니다. 원자료 전체, API key, 실행 cache, 개인정보가 포함된 파일과 중복 중간본은 공개 저장소에서 제외했습니다.

Drive 자료의 선별 기준과 반입 내역은 [자료 선별 인덱스](docs/DRIVE_SOURCE_INDEX.md)에서 확인할 수 있습니다.

