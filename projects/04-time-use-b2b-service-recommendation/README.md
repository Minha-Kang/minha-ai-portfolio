# Project 04. Time-Use-Based B2B Service Module Recommendation

**Completed · Spring 2026 · Service Intelligence team project**

통계청 MDIS 생활시간조사 데이터를 이용해 특정 고객군의 생활 문제를 정량화하고, 서비스 제공자가 우선 개발할 기능 모듈을 추천하는 프로젝트입니다. 기획자의 직관만으로 기능을 고르는 대신 생활시간, 가구·경제활동 조건과 주관적 상태를 하나의 계산 흐름으로 연결했습니다.

## Problem

같은 서비스 분야라도 1인 가구, 맞벌이 가구, 돌봄 가구와 고령층이 필요로 하는 기능은 다릅니다. 이 프로젝트는 고객 조건을 입력하면 공공데이터에서 유사 집단을 찾고, 해당 집단의 생활 패턴을 바탕으로 서비스 기능의 우선순위를 계산하는 것을 목표로 했습니다.

## Method

`Target profile → 28 variables → 8 life indices → Entropy-ROC weights → QFD matrix → 6 service modules`

1. 성별, 연령, 혼인, 가구, 자녀·돌봄, 소득, 직업과 경제활동 조건으로 타깃 집단을 정의했습니다.
2. 생활시간과 주관 상태를 포함한 28개 변수를 8개 생활지수로 구성했습니다.
3. PCA/요인 구조와 Cronbach's α로 지수 구성을 점검했습니다.
4. Entropy와 ROC 순위가중을 결합해 생활지수의 객관적 중요도를 계산했습니다.
5. 8개 WHAT 생활지수와 6개 HOW 서비스 모듈을 QFD 관계값 0·1·3·9로 연결했습니다.
6. `WHAT 중요도 × QFD 관계값`을 합산해 서비스 모듈의 우선순위를 산출했습니다.

## Eight life indices

- Subjective fatigue and time scarcity
- Repetition and routine management
- Mobility and accessibility
- Concurrent activity and multitasking
- Time pressure and obligatory activity
- Rest and spare-time use
- Health and sleep burden
- Child and household care

8개 지수의 Cronbach's α는 약 0.61-0.78 범위였습니다. 완전히 동일한 개념을 반복 측정하기보다 서로 다른 생활 신호를 묶은 탐색적 지수라는 점을 함께 고려해 해석했습니다.

## Six service modules

| Module | Role |
|---|---|
| Mobility / execution support | 이동, 예약, 체크인과 실제 행동 실행 지원 |
| Planning / structuring | 일정, 절차, 체크리스트와 우선순위 정리 |
| Reminder / action promotion | 필요한 시점의 알림과 행동 유도 |
| Record / feedback | 활동 기록, 진행률과 결과 피드백 |
| Sharing / social coordination | 가족·보호자·공동 사용자의 일정과 역할 조정 |
| Recommendation / personalization / transition | 상황에 맞는 선택과 다음 행동 추천 |

## Team results

- 6개 모듈 점수에 대한 PCA에서 PC1 설명률은 91.3%, PC1-PC3 누적 설명률은 98.0%였습니다.
- 모든 모듈이 공통적인 생활서비스 수요 축을 공유하면서도, 실행·조정·기록 등 보조적인 기능 차이가 있음을 확인했습니다.
- 최종 QFD 우선순위에서는 recommendation/personalization/transition support가 가장 높게 나타났습니다.
- 연도 및 고객 집단별로 모듈 필요도의 변화를 비교할 수 있는 구조를 제시했습니다.
- 사용자 조건을 선택하면 생활지수와 상위 서비스 모듈을 보여주는 추천 시뮬레이터 흐름을 구현했습니다.

이 결과는 수업 팀 프로젝트의 결과이며 개인 단독 성과가 아닙니다. QFD 관계값은 단순화된 설계값이므로 실제 제품 의사결정에 사용하려면 Delphi 조사, 사용자 만족도와 사용성 데이터로 추가 검증이 필요합니다.

## File

- [Final presentation - public version](docs/service-intelligence-final-public.pdf)

공개용 발표자료에서는 다른 팀원의 이름과 학번을 제거했습니다. MDIS 원자료와 편집 메모, 최종 8-index 구조와 일치하지 않는 초기 7-index prototype notebook은 포함하지 않았습니다.

