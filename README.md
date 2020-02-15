# Predict_Your_Next_Location_With_CNN

## 환경 설정
####  spec-file.txt 에 환경 세팅에 대해 모든 모듈버전을 명시해 놓았습니다.
######  This file may be used to create an environment using:
######  $ conda create --name 'env' --file 'this file'
######  platform: osx-64


## 모델 훈련 과정
####  1. 스포츠 트래커의 gpx 파일을 json 형태로 파싱한 json파일이 필요합니다.
  
<img width="309" alt="스크린샷 2020-02-15 오후 7 08 38" src="https://user-images.githubusercontent.com/48645552/74586062-1127f780-5027-11ea-8a51-ef01b65b5507.png">

속성 | 의미
:---: | :---:
`author` | gpx 데이터 주인 이름
`timestamp` | 시간
`timezone` | 시간 기준이 되는 위치
`latitude` | 위도
`longitude` | 경도

####  2. 
