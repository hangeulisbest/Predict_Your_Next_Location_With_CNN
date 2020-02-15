# Predict_Your_Next_Location_With_CNN

##  환경 설정
####  spec-file.txt 에 환경 세팅에 대해 모든 모듈버전을 명시해 놓았습니다.
######  This file may be used to create an environment using:
######  $ conda create --name 'env' --file 'this file'
######  platform: osx-64

##  모델 훈련 방법
#### training 과 test에 관한 자세한 설명은 HowToTraining.md 파일을 참고해주세요.
#### 

##  모델 사용 방법
####  1. 네이버 클라우드 플랫폼의 Web Dynamic map을 사용하므로 자신의 클라이언트 아이디를 준비합니다.
######  [네이버 클라우드 플랫폼의 클라이언트 아이디 발급](https://navermaps.github.io/maps.js.ncp/)
######  <pre><script type="text/javascript" src="https://openapi.map.naver.com/openapi/v3/maps.js?ncpClientId=yourId"></script><code>
####  2. 스포츠 트래커의 gpx 파일을 json 형태로 파싱한 json파일이 필요합니다. 아래의 사진과 같은 json 파일을 준비합니다.
  
<img width="309" alt="스크린샷 2020-02-15 오후 7 08 38" src="https://user-images.githubusercontent.com/48645552/74586062-1127f780-5027-11ea-8a51-ef01b65b5507.png">

속성 | 의미
:---: | :---:
`author` | gpx 데이터 주인 이름
`timestamp` | 시간
`timezone` | 시간 기준이 되는 위치
`latitude` | 위도
`longitude` | 경도

####  3. spec-file.txt 에 명시한 모듈을 모두 설치해 주세요.
######  `$ conda create --name env --file spec-file.txt`


####  4. 설치한 가상환경 `env`로 이동합니다.
######  `conda activate env`
######  만약 가상환경을 종료하려면
######  `conda deactivate`


####  5.


