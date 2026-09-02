# Google Drive 자료 선별·반입 인덱스

Google Drive와 최근 작업 파일에서 확인한 프로젝트 자료 중 공개 포트폴리오에 필요한 파일만 선별한 기록입니다.

## Final structure

| Project | Source candidates reviewed | Newly added | Files in project folder |
|---|---:|---:|---:|
| 01. Hotel Review Agentic AI | 93 | 18 | 24 |
| 02. Multi-Agent Failure Attribution | 27 | 3 | 7 |
| 03. AndroidControl UI Behavior & XAI | 35 | 5 | 6 |
| 04. Time-Use B2B Service Recommendation | 3 | 1 | 2 |
| **Total** | **158** | **27** | **39** |

## Selection rules

1. 최종 발표자료, 최종 보고서, 방법론, 검증 결과와 재현에 필요한 파일을 우선했습니다.
2. 같은 내용의 여러 버전은 최신·최종본 한 개만 남겼습니다.
3. 외부 benchmark의 원본 코드·논문은 직접 구현한 것으로 오해되지 않도록 제외했습니다.
4. API key, `.env`, cache, 전체 실행 log, raw dataset과 임시 파일은 제외했습니다.
5. 학번, 팀원 이름 등 개인정보가 포함된 자료는 공개용 사본으로 정리했습니다.
6. README와 방법이 일치하지 않는 초기 prototype은 최종 산출물로 공개하지 않았습니다.

## Project 01

- 연구 발표자료와 인수인계 문서
- 방법론·파이프라인 최적화·구조 비교 문서
- Gold 199/200 단계의 검증 workbook과 관리자 보고서
- 데이터 split과 감사 기록

현재 README의 Gold 350·2,643개 결과는 공개된 Gold 199/200 파일 이후의 연구 상태입니다. 최신 Gold 파일은 연구 진행 중이므로 아직 공개하지 않았습니다.

## Project 02

- 직접 작성한 분석보고서와 발표자료 2종
- 직접 만든 task·split·domain 요약 CSV 3종

원 Who&When benchmark 코드, 논문 PDF와 전체 trajectory는 제외했습니다.

## Project 03

- Agent 행동 기반 UI 가독성 보고서·발표·그래프 부록
- 개인정보를 제거한 XAI 최종 발표자료와 발표 스크립트

팀 XAI 프로젝트는 강민하의 실제 기여인 데이터 전처리·보고서 작성(22.5%)을 README에 명시했습니다.

## Project 04

- 최종 발표자료 20페이지의 공개용 PDF 1개
- 첫 페이지의 다른 팀원 이름과 전체 학번을 제거

편집 지시만 담긴 DOCX는 산출물이 아니므로 제외했습니다. 별도 Streamlit notebook은 7개 생활지수를 사용하는 초기 prototype으로, 최종 발표와 CV/PR의 8개 생활지수 구조와 달라 제외했습니다. MDIS raw microdata도 공개하지 않았습니다.

## Notes

공개 저장소만으로 모든 프로젝트의 end-to-end 재실행을 보장하지 않습니다. 제외된 입력 데이터, 외부 문헌, API 환경 또는 비공개 연구 파일이 필요한 경우가 있습니다. 팀 프로젝트의 결과는 개인 기여 범위와 구분해 적었습니다.

