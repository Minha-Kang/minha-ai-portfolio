# Project 04. Agent Behavior–Based UI Readability Analysis with AndroidControl

*AndroidControl Agent 행동을 활용한 UI 가독성·행동 복잡도 분석*

AndroidControl Agent trajectory를 활용해 앱 화면과 행동 분포의 복잡도를 정량화하고, 이를 UI 가독성 평가 특성으로 연결한 EDA·연구 설계 프로젝트입니다.

## 연구 질문

- Agent가 특정 화면에서 반복·분산된 행동을 보이는 현상을 UI 복잡도의 신호로 사용할 수 있는가?
- 앱 화면이 아닌 system/transition step을 제거하면 행동·page type label의 품질이 개선되는가?
- 화면 특성과 행동 entropy를 결합해 사람이 읽기 어려운 UI를 설명할 수 있는가?

## 데이터 정제와 분석

| 단계 | 결과 |
|---|---:|
| 원본 | 46,022 step / 8,456 episode |
| 앱 화면 중심 정제본 | 6,258 episode |
| Episode-level UNKNOWN | 0.628 → 0.429 |
| Step-level UNKNOWN | 0.535 → 0.359 |

- page type, action type, episode step 수, 화면 전환 분포 분석
- 앱 외부 화면·불완전 episode를 구분하는 정제 규칙 적용
- 화면별 행동 분포와 entropy를 UI 복잡도 후보 특성으로 설계
- CNN page type, Agent 행동 특성, 화면·행동 entropy를 결합하는 후속 모델 구조 제안

## 프로젝트 기여

단순히 screenshot의 시각적 요소만 평가하지 않고, **그 화면에서 Agent가 어떻게 행동했는지**를 가독성 신호로 추가했습니다. 데이터 품질 문제를 UNKNOWN 비율로 먼저 확인하고, 정제 전후 수치를 함께 제시해 특성 설계의 근거를 남겼습니다.

## 현재 단계와 공개 범위

이 저장소에는 원본 AndroidControl 데이터나 학습 코드가 아니라 EDA 결과와 연구 구조를 요약했습니다. 위 수치는 정제 파이프라인의 데이터 품질 결과이며, 아직 최종 사용자 가독성 점수의 예측 성능을 의미하지 않습니다.

## 대표 원본

- [UI 가독성 연구 최종 발표](https://docs.google.com/presentation/d/1OBa4lxXBavsfiz1hSTlRcdbDkDNEcOS_/edit)
- [사용자 행동 분포 수렴성 기반 UI 가독성 연구 보고서](https://docs.google.com/document/d/19trZtnauEYFUX7EeOqpYNM2L6rS6aj2c/edit)
- [AndroidControl EDA 발표자료](https://docs.google.com/presentation/d/1rQmc6DQkeQVHAqAx03Lq8FXNJ8XIm0Rq/edit)

Drive 링크는 공유 설정에 따라 별도 접근 권한이 필요할 수 있습니다.
