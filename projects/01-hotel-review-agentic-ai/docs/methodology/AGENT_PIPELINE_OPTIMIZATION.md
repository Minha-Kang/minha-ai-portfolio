# Agent 1–6 실행시간 최적화안

## 결론

기존 1,000개 결과는 다시 돌리지 않는다. 완료된 Agent 1–5 산출물을 재사용하고, 호텔별 IPA에서 확인된 **안정 Q2 호텔×Feature×Journey 15개 그룹만 Agent 6에 전달**하는 것이 현재 최선이다.

- 기존 Agent 6 API 단위: 1,321개 impact
- 변경 후 Agent 6 API 단위: 안정 Q2 15개 그룹
- 호출 단위 감소: 98.9%
- 그룹당 개선안: 최대 2개
- 최종 개선안 수: 최대 30개
- 기존 8,258개의 산발적 개선안을 교수에게 설명 가능한 호텔별 우선과제로 압축

## 실제 로그에서 확인된 병목

| 구간 | 기존 실행량 | 로그상 시간/규모 | 문제 |
|---|---:|---:|---|
| Agent 1–4 | 모델 호출 4,685회 | 약 6.8시간 | 리뷰 1,000개 순차 처리, specialist 재호출 685회 |
| Agent 5 | 결정론적 계산 | 미미함 | 주요 병목 아님 |
| Agent 6 | impact 1,321개 순차 호출 | 성공 latency 합 약 7.47시간, 약 646만 token | 8,258개 개선안 생성으로 과잉 처리 |

## 코드 변경 내용

`run_full1000_agent1_6.py`에 다음 옵션과 동작을 추가했다.

1. `--resume`
   - canonical Agent 1–4 결과가 1000/1000 완료이면 즉시 재사용한다.
   - 병렬 worker 폴더가 없더라도 완료된 1,000개를 다시 돌리지 않는다.

2. `--agent14-workers N`
   - 리뷰 길이를 기준으로 작업량을 균등 분배한다.
   - worker별 상태·로그를 분리하고 종료 후 기존 형식으로 병합한다.
   - 권장 시작값은 3이다. rate limit이 발생하면 2로 낮춘다.

3. `--agent14-profile quality|fast`
   - `quality`: 기존 재검증·재호출 규칙을 유지한다. 기본값이다.
   - `fast`: 각 specialist를 1회로 제한해 기존 로그의 재호출 685회를 제거한다.
   - `fast`는 Gold 199에서 기존 quality 결과와 비교한 뒤에만 전체 데이터에 사용한다.

4. `--stop-after-agent5`
   - Agent 1–5까지만 만들고 종료한다.
   - 이후 로컬 IPA로 안정 Q2를 정할 때 Agent 6 비용을 발생시키지 않는다.

5. `--priority-agent6-csv`
   - `stable_q2_journey_drilldown.csv`의 호텔×Feature×Journey만 Agent 6에 보낸다.
   - 같은 그룹에 속한 여러 리뷰 근거를 최대 8개까지 함께 전달한다.
   - 그룹별 최대 2개 조치만 생성하고, review ID·impact ID를 모두 보존한다.
   - 입력 내용의 hash를 확인하므로 동일 입력은 cache에서 재사용한다.

## 현재 1,000개에 적용하는 명령

이미 Agent 1–5가 완료되어 있으므로 아래 명령은 Agent 1–4를 건너뛰고 안정 Q2 15개 그룹만 Agent 6에 전달한다.

```powershell
python run_full1000_agent1_6.py `
  --resume `
  --agent14-profile quality `
  --agent14-workers 3 `
  --priority-agent6-csv "C:\Users\Administrator\Documents\Codex\2026-08-15\new-chat\outputs\hotel-ipa-prototype\stable_q2_journey_drilldown.csv" `
  --agent6-max-actions 2
```

API를 전혀 쓰지 않으려면 이 명령도 실행하지 않고, 이미 만든 `priority_action_traceability.csv`의 기존 Agent 6 개선안을 그대로 사용한다. 현재 논문·교수 보고에는 이 무과금 경로로도 충분하다.

## 다음 신규 1,000개 실행 순서

### 1단계: Agent 1–5만 실행

```powershell
python run_full1000_agent1_6.py `
  --resume `
  --agent14-profile quality `
  --agent14-workers 3 `
  --stop-after-agent5
```

### 2단계: 로컬 IPA 및 bootstrap

API 없이 호텔별 Q1–Q4와 안정 Q2를 만든다. 최소 표본수와 bootstrap 기준을 통과하지 못한 그룹은 Agent 6 대상에서 제외한다.

### 3단계: 안정 Q2만 Agent 6 실행

```powershell
python run_full1000_agent1_6.py `
  --resume `
  --agent14-profile quality `
  --agent14-workers 3 `
  --priority-agent6-csv "경로\stable_q2_journey_drilldown.csv" `
  --agent6-max-actions 2
```

## 예상 시간

실측이 아니라 기존 로그에 근거한 추정치다.

| 실행 방식 | 예상 wall time | 품질/비용 특성 |
|---|---:|---|
| 기존 순차 전체 실행 | 약 13시간 | Agent 6 과잉 호출 |
| quality + worker 3 + priority Agent 6 | 약 2.4시간, rate limit 포함 시 2.5–3시간 예상 | Agent 1–4 품질 규칙 유지 |
| fast + worker 3 + priority Agent 6 | 약 2.0시간 전후 | 호출 감소, Gold 199 검증 필수 |
| 현재 완료 결과 재사용 + 기존 개선안 매칭 | 약 25초 | API 비용 0원, 현재 권장 |

병렬화는 시간을 줄이지만 Agent 1–4 token 비용 자체는 줄이지 않는다. 비용 절감의 핵심은 Agent 6 대상 축소이며, `fast`는 검증 후 추가로 적용할 수 있다.

## 검증 기준

`fast`를 채택하려면 Gold 199에서 다음을 quality 기준과 비교한다.

- Evidence span 누락률
- Feature macro/micro F1
- Journey stage F1
- sentiment MAE 또는 일치율
- FinalVerifier 통과율
- 문제 label 수와 안정 Q2 호텔 그룹의 변화

안정 Q2 구성이나 핵심 지표가 유의하게 달라지면 `fast`를 쓰지 않고 `quality + 병렬 worker`만 사용한다.

