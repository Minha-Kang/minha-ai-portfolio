# Hotel Dynamic Orchestrator v8

이 버전은 v7의 Feature taxonomy와 Evidence·Feature 역할을 유지하되,
Journey를 호텔 Guest Cycle 4단계로 교체한다. `J00`은 강제 오분류를 막는
보조 어노테이션 값이므로 연구상 Journey 단계 수는 4개, 출력 가능 코드는
총 5개다.

| 코드 | Guest Cycle | 적용 범위 |
|---|---|---|
| J00 | Unspecified / Overall | 리뷰 근거만으로 시점을 특정할 수 없음 |
| J01 | Pre-arrival | 예약, 변경·취소, 방문 전 문의 |
| J02 | Arrival | 접근, 도착, 첫 응대, 체크인 |
| J03 | Occupancy | 객실, 청결, 수면, 식음, 시설, 체류 중 대응 |
| J04 | Departure | 체크아웃, 결제, 보증금, 퇴실·짐 보관 |

## v7과의 핵심 차이

| 항목 | v7 Orchestrator | v8 Dynamic Orchestrator |
|---|---|---|
| Controller 개입 | 초기 4개 Agent는 고정 순서, Verifier 이후 재검토에서만 실질 선택 | 첫 Evidence 이후부터 매 단계 상태 기반 선택 |
| Controller 입력 | 주로 Verifier 요청과 호출 수 | 전체 산출물, 신뢰도, 수량 불일치, Verifier 요청, Guardrail, 최근 route |
| 재호출 | 선택 후 downstream 고정 chain | Controller가 다음 단계를 다시 선택 |
| 상위 Agent 재호출 | 하위 산출물을 chain으로 덮어씀 | 하위 산출물을 즉시 무효화하여 stale state 차단 |
| `target_mentions` | 구조적으로 거의 미사용 | Specialist 재검토 지시문에 반영 |
| 종료 | Verifier의 자체 요청에 크게 의존 | Verifier 최소 1회 + Controller 종료 승인 + 호출 예산 |

이 구조는 무제한 자율 실행이 아니라 **bounded autonomy**다. Agent가 route를
선택하지만 다음 조건은 코드가 강제한다.

- `MultiFeatureMapper`는 Evidence가 생성된 뒤에만 호출
- `SentimentJourneyScorer`는 Feature mapping 뒤에만 호출
- `FinalVerifier`는 세 Specialist 산출물 뒤에만 호출
- `END`는 FinalVerifier 결과가 있을 때만 허용
- Verifier의 구체적이고 실행 가능한 재검토 요청은 최소 한 번 처리한 뒤 종료
- Agent별 호출 수, 전체 Specialist 단계, Controller 단계에 상한 적용

## 파일

- `hotel_dynamic_orchestrator_v8.py`: 동적 정책, 상태 진단, 무효화, 종료 게이트
- `hotel_guest_cycle_v8.py`: J01~J04와 J00 경계 및 보수적 시점 추론
- `hotel_architecture_common_v8.py`: Guest Cycle schema, Scorer, Verifier, Guardrail
- `architecture_graphs_v8.py`: LangGraph 연결
- `run_architecture_compare_v8.py`: 기존 v7 입출력을 재사용하는 실행 래퍼
- `test_guest_cycle_v8.py`: 5개 코드와 핵심 Journey 경계 회귀 테스트
- `test_dynamic_orchestrator_v8.py`: API 호출 없는 라우팅 회귀 테스트

같은 폴더에 기존 `hotel_architecture_common_v7.py`와
`run_architecture_compare_v7.py`가 있어야 한다.

## 실행

```bash
python run_architecture_compare_v8.py \
  --input "/content/drive/MyDrive/Portfolio/hotel/hotel_gold_label_200_full_reaudit_final.xlsx" \
  --limit 10 \
  --resume
```

로컬에서는 코드 폴더의 `.env.local`에 `OPENAI_API_KEY`가 있어야 한다.
`.env.local`은 Drive에 업로드하지 않는다.

## 주요 환경 변수

```text
DYNAMIC_MAX_CALLS_EVIDENCE=3
DYNAMIC_MAX_CALLS_MAPPER=3
DYNAMIC_MAX_CALLS_SCORER=3
DYNAMIC_MAX_CALLS_VERIFIER=3
DYNAMIC_MAX_SPECIALIST_STEPS=12
DYNAMIC_MAX_CONTROLLER_STEPS=16
DYNAMIC_CONTROLLER_MAX_STATE_CHARS=24000
```

199개 비교 실험에서는 먼저 10개 smoke test를 실행하고, route log에서 다음을
점검한 뒤 전체 실행한다.

1. 초기 필수 단계가 빠지지 않았는가
2. 재호출 이유와 target mention이 구체적인가
3. 상위 Agent 재호출 뒤 downstream 산출물이 새로 생성됐는가
4. 같은 Agent를 근거 없이 반복 호출하지 않는가
5. v7 대비 FeatureStage F1 개선이 추가 token·시간 비용을 정당화하는가
