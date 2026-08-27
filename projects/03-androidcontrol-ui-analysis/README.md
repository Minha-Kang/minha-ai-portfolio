# Project 03. AndroidControl UI Readability & XAI Complexity Analysis

AndroidControl 데이터를 활용한 두 UI 연구를 하나의 프로젝트로 통합했습니다.

1. **Agent 행동 기반 UI 가독성 분석** — 화면에서 나타나는 Agent 행동 분포와 entropy를 UI 복잡도의 신호로 설계
2. **XAI 기반 쇼핑 UI 복잡도 진단** — 화면·구조 특성의 예측 기여를 설명하고 실제 UI 개선 방향으로 연결

두 분석은 접근 방식은 다르지만, 화면을 단순히 시각적으로 묘사하는 데서 끝나지 않고 **어떤 UI가 왜 어렵고 무엇을 개선해야 하는지 설명하는 것**을 공통 목표로 합니다.

## 1. Agent 행동 기반 UI 가독성 분석

### 연구 질문

- Agent가 특정 화면에서 반복적이거나 분산된 행동을 보이는 현상을 UI 복잡도의 신호로 사용할 수 있는가?
- 앱 화면이 아닌 system·transition step을 제거하면 행동·page type label의 품질이 개선되는가?
- 화면 특성과 행동 entropy를 결합해 읽기 어려운 UI를 설명할 수 있는가?

### 데이터 정제와 분석

| 단계 | 결과 |
|---|---:|
| 원본 | 46,022 step / 8,456 episode |
| 앱 화면 중심 정제본 | 6,258 episode |
| Episode-level UNKNOWN | 0.628 → 0.429 |
| Step-level UNKNOWN | 0.535 → 0.359 |

- page type, action type, episode step 수와 화면 전환 분포 분석
- 앱 외부 화면·불완전 episode를 구분하는 정제 규칙 적용
- 화면별 행동 분포와 entropy를 UI 복잡도 후보 특성으로 설계
- CNN page type, Agent 행동 특성, 화면·행동 entropy를 결합하는 후속 모델 구조 제안

이 수치는 정제 파이프라인의 데이터 품질 결과이며, 최종 사용자 가독성 점수의 예측 성능을 의미하지 않습니다.

### 산출물

- [UI 가독성 연구 최종 발표](behavior-analysis/docs/ui-readability-final-presentation.pptx)
- [사용자 행동 분포 수렴성 기반 UI 가독성 연구 보고서](behavior-analysis/docs/ui-readability-final-report.docx)
- [UI 가독성 전체 그래프 부록](behavior-analysis/results/ui-readability-graph-appendix.pptx)

## 2. XAI 기반 쇼핑 UI 복잡도 진단

### 문제 정의

UI 복잡도 모델이 단순히 “복잡하다”는 점수만 출력하면 디자이너가 무엇을 바꿔야 하는지 알기 어렵습니다. 이 팀 프로젝트는 화면의 시각·구조 특성과 모델 설명을 연결해, 복잡도를 높이거나 낮추는 요소를 구체적인 개선 방향으로 해석하는 것을 목표로 했습니다.

### 분석 범위

- AndroidControl의 쇼핑 관련 1,531개 episode와 8,651개 screenshot 분석
- 구조·텍스트·상호작용·레이아웃·균형·쇼핑 의미를 포함한 UI 특성 구성
- White-box, image-only, metadata-only와 fusion model 비교
- SHAP 기반 feature importance와 dependence 분석
- 화면 유형별 복잡도 유발·완화 요인을 실제 UI 사례에 연결

이 프로젝트에서 강민하는 **주제 선정, 선행연구 조사와 발표 구성**을 담당했습니다. 모델링 결과는 수업 팀 프로젝트의 분석 결과이며, 상용 시스템 배포 성능을 의미하지 않습니다.

### 산출물

- [XAI 최종 발표자료 — 공개용](xai/docs/xai-final-presentation-public.pdf)
- [12분 영어 발표 스크립트](xai/docs/xai-presentation-script.docx)

공개용 발표자료에서는 학번과 팀원 이름을 제거하고, 기여 역할 표는 익명화했습니다.

## 파일 구성

```text
03-androidcontrol-ui-analysis/
├── README.md
├── behavior-analysis/
│   ├── docs/
│   │   ├── ui-readability-final-presentation.pptx
│   │   └── ui-readability-final-report.docx
│   └── results/
│       └── ui-readability-graph-appendix.pptx
└── xai/
    └── docs/
        ├── xai-final-presentation-public.pdf
        └── xai-presentation-script.docx
```

이 폴더에는 README를 포함해 6개 파일이 있습니다. 원본 AndroidControl dataset, 중간 발표본, 중복 스크립트, 학번·팀원 이름이 포함된 XAI 원본 PDF는 공개 저장소에서 제외했습니다. 선별 근거는 [Drive 자료 선별 인덱스](../../docs/DRIVE_SOURCE_INDEX.md)에서 확인할 수 있습니다.
