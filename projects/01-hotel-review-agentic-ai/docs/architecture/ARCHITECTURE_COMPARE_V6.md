# Hotel Review Agent AI — 6-Agent Architecture Comparison v6

## 목적

동일한 6개 Agent 역할을 유지한 상태에서 다음 세 architecture를 공정하게 비교합니다.

1. `sequential`
2. `sequential_feedback`
3. `orchestrator`

세 조건은 같은 모델, 같은 Feature 10개, 같은 Stage 6개, 같은 구조화 출력 schema를 사용합니다. 달라지는 것은 Agent를 호출하고 재검토하는 방식뿐입니다.

## 엄격한 입력 조건

리뷰 단위 Agent 1~4와 OrchestratorController에는 **리뷰 본문만** 제공합니다.

제공하지 않는 정보:

- Gold 근거문장
- Gold Feature
- Gold Stage
- Gold 감성
- 리뷰 제목
- 별점

리뷰 제목과 별점은 Agent 실행 후 결과표에 다시 붙입니다. 별점은 Agent 1~4가 끝난 뒤 Agent 5의 데이터셋 분석에서 처음 사용합니다. Gold Label은 `evaluate_single_architecture_v6.py`에서만 읽습니다.

`run_architecture_compare_v6.py`는 `Gold_리뷰_200`을 읽은 직후 실행용 DataFrame을 다음 네 열로 축소합니다.

```text
골드라벨ID
평점             # Agent state에는 넣지 않고 사후 결과표에만 연결
리뷰제목         # Agent state에는 넣지 않고 사후 결과표에만 연결
리뷰원문         # Agent 1~4와 controller의 유일한 내용 입력
```

## 핵심 6 Agent

### 리뷰 단위

1. `EvidenceExtractor`
2. `MultiFeatureMapper`
3. `SentimentJourneyScorer`
4. `FinalVerifier`

### 데이터셋 단위

5. `RatingImpactAnalyzer`
6. `ImprovementRecommendationAgent`

`FeedbackRouter`와 `OrchestratorController`는 Label을 생성하지 않는 control layer입니다. 핵심 6 Agent 수에 포함하지 않습니다.

## Architecture 정의

### Sequential

```text
EvidenceExtractor
→ MultiFeatureMapper
→ SentimentJourneyScorer
→ FinalVerifier
→ END
```

모든 리뷰가 고정 순서를 한 번 통과합니다.

### Sequential + Feedback

```text
Evidence → Feature → Sentiment/Journey → Verifier
                                          ├─ 통과 → END
                                          └─ 오류 → 기존 Specialist 1개 재호출
                                                     → downstream 재실행
                                                     → Verifier → END
```

별도 Feedback Agent를 추가하지 않습니다. FinalVerifier의 구조화된 요청에 따라 기존 Agent 1~3 중 하나를 최대 한 번 재호출합니다.

### Orchestrator

```text
OrchestratorController
↔ EvidenceExtractor / MultiFeatureMapper / SentimentJourneyScorer / FinalVerifier
→ END
```

Controller는 다음 Specialist 선택, 재작업 범위, 종료 여부만 판단합니다. 직접 Feature·감성 Label을 만들 수 없습니다.

가드레일:

- FinalVerifier 없이 종료 금지
- Specialist당 재호출 최대 1회
- Specialist 호출 최대 8회
- Controller 호출 최대 10회
- 잘못된 route는 허용 경로로 자동 교정
- 재검토 후 downstream Agent와 FinalVerifier를 다시 실행

## 폴더 배치

압축을 풀어 다음 폴더 전체를 Google Drive에 넣습니다.

```text
/content/drive/MyDrive/Portfolio/hotel/hotel_architecture_compare_v6_package/
```

Gold 파일은 다음 위치에 둡니다.

```text
/content/drive/MyDrive/Portfolio/hotel/hotel_gold_label_200_full_reaudit_final.xlsx
```

노트북:

```text
hotel_agent_architecture_compare_v6.ipynb
```

## 실행 순서

### 1. Mock 3개

```bash
python run_six_agent_architecture_pipeline_v6.py \
  --input hotel_gold_label_200_full_reaudit_final.xlsx \
  --output_dir outputs_architecture_compare_v6_mock \
  --architectures sequential,sequential_feedback,orchestrator \
  --limit 3 \
  --mock
```

### 2. 실제 API 5개

```bash
python run_six_agent_architecture_pipeline_v6.py \
  --input hotel_gold_label_200_full_reaudit_final.xlsx \
  --output_dir outputs_architecture_compare_v6_real5 \
  --architectures sequential,sequential_feedback,orchestrator \
  --limit 5 \
  --skip_improvement_llm \
  --fail_fast
```

### 3. 난도 균형 40개

```bash
python make_balanced_architecture_sample_v6.py \
  --gold hotel_gold_label_200_full_reaudit_final.xlsx \
  --output architecture_sample_40_ids.txt

python run_six_agent_architecture_pipeline_v6.py \
  --input hotel_gold_label_200_full_reaudit_final.xlsx \
  --output_dir outputs_architecture_compare_v6_40 \
  --architectures sequential,sequential_feedback,orchestrator \
  --id_file architecture_sample_40_ids.txt \
  --skip_improvement_llm \
  --resume
```

### 4. 199개 전체

```bash
python run_six_agent_architecture_pipeline_v6.py \
  --input hotel_gold_label_200_full_reaudit_final.xlsx \
  --output_dir outputs_architecture_compare_v6 \
  --architectures sequential,sequential_feedback,orchestrator \
  --resume
```

## 주요 산출물

각 architecture 폴더:

```text
00_input_leakage_audit.csv
01_agent_predictions_review.csv
02_agent_predictions_labels.csv
03_agent_step_logs.csv
04_orchestrator_route_logs.csv
05_runtime_metrics.csv
06_run_manifest.json
04_review_level_evaluation.csv
05_label_level_evaluation.csv
06_summary_metrics.csv
07_feature_metrics.csv
08_stage_metrics.csv
09_error_cases.csv
10_verifier_change_metrics.csv
11_feature_rating_summary.csv
12_feature_stage_rating_summary.csv
13_rating_model_importance.csv
14_improvement_priority_inputs.csv
15_rating_agent_report.json
16_improvement_recommendations.csv
17_manager_report.md
18_dataset_agent_logs.csv
19_dataset_agent_summary.json
```

전체 비교 폴더:

```text
30_architecture_quality_comparison.csv
31_architecture_operational_comparison.csv
32_complexity_group_metrics.csv
33_downstream_priority_stability.csv
34_architecture_selection_support.csv
35_v6_pipeline_summary.json
```

## 평가 기준

품질:

- Feature Micro/Macro F1
- Feature Exact Set Match
- Feature–Stage Micro/Macro F1
- Feature–Stage Exact Set Match
- 감성 방향·점수·MAE
- Evidence 원문 존재율
- Gold evidence 유사도
- 누락 및 과잉 Label

운영:

- Agent 호출 수
- Controller 호출 수
- 토큰 수
- 실행시간
- 오류율
- routing 가드레일 교정률
- 입력 누수 위반 수

리뷰 난도:

- 단순: Gold Label 1~2개
- 보통: 3~4개
- 복합: 5개 이상
- 경계형: F03/F04/F05/F07 중 둘 이상
- 혼합형: 동일 Feature–Stage에 긍정·부정 공존

## 선택 원칙

Orchestrator라는 이름만으로 선택하지 않습니다.

- Sequential 대비 Feature–Stage Micro F1 약 2%p 이상 개선 여부
- 복합·경계 리뷰에서 Exact Match와 누락 감소 여부
- 추가 호출·토큰·시간이 개선 폭에 비해 과도한지
- routing 오류와 반복 종료 문제가 있는지

Agent 5의 중요도는 예측 연관성이며 인과효과가 아닙니다.
