# Project 03. AndroidControl UI Behavior Analysis & XAI Diagnostics

**Completed · Jan. - Jun. 2026**

AndroidControl 데이터를 사용해 진행한 두 작업을 한 폴더에 정리했습니다. 첫 번째는 Agent의 행동 기록을 분석 가능한 표로 만드는 탐색적 연구였고, 두 번째는 UI 복잡도를 예측하고 설명한 수업 팀 프로젝트입니다.

## 1. Agent behavior analysis

### What I did

- goal, instruction, action, screenshot, accessibility tree를 episode·step 단위로 연결
- screenshot hash 변화로 화면 transition indicator 구성
- 1,000개 episode와 624개 app을 대상으로 step table, episode summary, app catalog 작성
- 앱 외부 화면과 불완전 episode를 구분해 page/action label 정제
- 행동 분포와 entropy를 UI 복잡도 후보 신호로 검토

### Data cleaning result

| Item | Before | After |
|---|---:|---:|
| Episodes | 8,456 | 6,258 app-centered episodes |
| Episode-level UNKNOWN | 0.628 | 0.429 |
| Step-level UNKNOWN | 0.535 | 0.359 |

UNKNOWN 감소는 정제 규칙의 결과이며, 사용자 가독성 점수의 예측 성능을 의미하지 않습니다.

### Files

- [UI readability presentation](behavior-analysis/docs/ui-readability-final-presentation.pptx)
- [UI readability report](behavior-analysis/docs/ui-readability-final-report.docx)
- [Graph appendix](behavior-analysis/results/ui-readability-graph-appendix.pptx)

## 2. Team XAI study

AndroidControl의 쇼핑 UI를 대상으로 시각·구조 특성이 복잡도 예측에 어떻게 기여하는지 분석한 팀 프로젝트입니다.

### Dataset and method

- 1,531 episodes, 8,651 screenshot/JSON records
- 45개 structural UI feature 구성, pruning과 VIF 이후 28개 사용
- episode-based train/test split으로 같은 episode의 화면이 양쪽에 섞이는 문제 방지
- image-only, metadata-only, fusion model 비교
- Ridge/Lasso coefficient와 SHAP을 사용한 구조 해석

### Team results

| Model | R² | MSE |
|---|---:|---:|
| Image-only | 0.8901 | 0.0389 |
| Fusion | 0.7818 | 0.0772 |
| Metadata-only | -28.3771 | 10.3953 |

위 성능은 팀 전체 결과입니다. 제 기여는 **데이터 전처리와 보고서 작성(22.5%)**이었으며, 모델링 결과를 개인 단독 성과로 표현하지 않습니다.

### Files

- [Public final presentation](xai/docs/xai-final-presentation-public.pdf)
- [English presentation script](xai/docs/xai-presentation-script.docx)

공개 발표자료에서는 학번과 팀원 이름을 제거했습니다. 원본 dataset, 중간 발표본, 개인정보가 포함된 원본 PDF는 포함하지 않았습니다.

