# Validation Report — 2026-08-02

## 완료된 검사

- Python 구문 검사: 통과
- 전체 자동 테스트: 26개 통과
- API 없는 Pilot 20 준비 실행: 통과
- Pilot 입력 원문 병합: 20/20 존재
- Pilot Agent 1~4 예측 라벨: 84개
- Pilot Agent 5 상위 문제군: 5개
- CLEAN_HOTEL 1,000 고정 입력 파일 로딩: 통과
- CLEAN_HOTEL → v8.2 Agent 1~4 모의 실행: 2/2 성공
- Agent 1~4 모의 결과 → Agent 5 full1000 어댑터: 통과
- 결과 Excel 8종 생성 및 재로딩: 통과
- OpenAI Responses API 구조화 출력 인자 호환성: 확인

## 아직 실행하지 않은 검사

`OPENAI_API_KEY`가 연결되지 않았으므로 Agent 6, 문헌 임베딩 검색,
RAG Judge의 실제 API 호출은 실행하지 않았습니다. 결제와 키 연결 후
`python hotel_agent56_pipeline.py --mode pilot20`을 실행하면 JSONL 상태 파일을
기준으로 중단 지점부터 재개됩니다.

## Pilot 20 고정 ID

GL065, GL192, GL190, GL079, GL018, GL057, GL164, GL042, GL197, GL193,
GL170, GL087, GL191, GL048, GL097, GL003, GL001, GL052, GL061, GL064

