# Project 07–08. 머신러닝·딥러닝 미니 프로젝트

분류·이미지·시계열 문제를 통해 전처리, 모델 구조 비교, 성능 해석과 결과 시각화를 연습한 프로젝트 모음입니다.

## Project 07. UCI HAR 인간행동 인식

### 목표

스마트폰 가속도계·자이로스코프에서 추출한 특성으로 일상 행동 6개를 분류하고, 모델별 성능과 오류 패턴을 비교했습니다.

### 데이터와 방법

- 참가자 30명
- 전체 표본 10,299개
- 입력 특성 561개
- 분류 대상: WALKING, WALKING_UPSTAIRS, WALKING_DOWNSTAIRS, SITTING, STANDING, LAYING
- 비교 모델: SVM, Logistic Regression, Neural Network

### 담당 범위

팀 프로젝트에서 데이터 구조 확인, 모델 비교, 결과 해석과 발표 자료 정리를 수행했습니다. 단순 정확도뿐 아니라 행동 간 혼동이 발생하는 패턴을 비교하는 데 초점을 두었습니다.

## Project 08. MNIST · RNN KOSPI

### MNIST 이미지 분류

- PyTorch 기반 Fully Connected Network와 Convolutional Neural Network 구성
- 60,000개 학습 데이터와 10,000개 테스트 데이터 사용
- 구조 차이가 이미지의 공간 정보 활용에 미치는 영향 비교
- 분류 결과와 모델 활용 사례를 발표 자료로 정리

### RNN KOSPI 시계열 예측

- Open·High·Low·Volume을 포함한 과거 5일 입력으로 다음 날 Close 예측
- PyTorch 기반 Vanilla RNN 시계열 모델 구현
- 실제값과 예측값 그래프를 통해 추세 추종과 오차 해석

## 공개 범위

현재 저장소에는 과제 원본 코드·데이터·정량 성능표 대신 문제 설정, 모델 구성과 수행 범위를 요약했습니다. 따라서 재현 가능한 benchmark 패키지라기보다 머신러닝 수업 프로젝트의 경험과 분석 관점을 보여주는 자료입니다.

## Drive 원본 파일명

- `AI_Practice_MNIST_강민하.pptx`
- `과제6_강민하_RNN_KOSPI_실행결과반영_최종.pptx`
- UCI HAR 팀프로젝트 분석 자료
