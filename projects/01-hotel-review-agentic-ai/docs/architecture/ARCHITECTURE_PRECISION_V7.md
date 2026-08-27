# Hotel Review Agent AI — Precision-first v7

## 목적

v6 Sequential 116개 개발 결과에서 확인된 핵심 문제는 근거 탐색 실패가 아니라 과잉 Label, Feature·Stage 경계, J99, 동일 Feature+Stage 중복이었다. v7은 이 오류를 줄이기 위해 Sequential과 Orchestrator만 비교한다.

## 실험 무결성

116개 결과를 보고 prompt와 guardrail을 조정했으므로 GL001~GL116은 개발 세트다. 개선 효과의 1차 평가는 이전에 사용하지 않은 holdout 83개에서 수행해야 한다. 기존 v6 116개 결과와 v7 결과를 합쳐 최종 점수로 보고하면 안 된다.

## 6개 Agent

1. EvidenceExtractor
2. MultiFeatureMapper
3. SentimentJourneyScorer
4. FinalVerifier
5. RatingImpactAnalyzer
6. ImprovementRecommendationAgent

OrchestratorController와 PrecisionGuardrail은 제어 계층이며 핵심 Agent 수에 포함하지 않는다.

## 주요 개선

- EvidenceExtractor가 단순 존재·시설 목록을 근거로 뽑지 않도록 precision-first gate 추가
- F10 객실 비품, F09 직원 태도, F06 주변 식당 경계 강화
- 중립은 명시적 중립 평가에만 사용하고 mere description은 삭제
- J99 금지 및 Feature별 허용 Stage 강제
- FinalVerifier는 새 Label을 직접 창작하지 않고 누락은 review request로만 기록
- 동일 Feature+Stage를 deterministic하게 하나로 병합
- evidence 원문 포함 검사
- Billing 비활성화 등 영구 API 오류는 첫 발생에서 즉시 중단
- atomic CSV 저장, resume 시 OK 행만 보존하고 ERROR 중복 제거

## 권장 실행

### 1. split 생성

```bash
python make_dev_holdout_split_v7.py \
  --gold hotel_gold_label_200_full_reaudit_final.xlsx \
  --output_dir splits_v7
```

### 2. holdout 83개, 두 구조 실행

```bash
python run_two_architecture_pipeline_v7.py \
  --input hotel_gold_label_200_full_reaudit_final.xlsx \
  --output_dir outputs_architecture_precision_v7_holdout83 \
  --architectures sequential,orchestrator \
  --id_file splits_v7/holdout_83_ids.txt \
  --resume
```

### 3. 구조 선택 후 전체 199개 재실행

Prompt가 바뀌었으므로 기존 v6 성공 116개를 재사용하지 않는다.

```bash
python run_two_architecture_pipeline_v7.py \
  --input hotel_gold_label_200_full_reaudit_final.xlsx \
  --output_dir outputs_architecture_precision_v7_full199 \
  --architectures sequential,orchestrator \
  --resume
```

## 기대와 한계

기존 116개 출력에 deterministic guardrail만 재적용한 개발용 replay에서 Feature+Stage Micro Precision은 약 0.563에서 0.635로, Micro F1은 약 0.644에서 0.691로 상승했다. 이는 prompt 개선 전 기존 출력에 대한 후처리 추정치이며, 실제 개선 성능은 holdout 83개 결과로 판단해야 한다.
