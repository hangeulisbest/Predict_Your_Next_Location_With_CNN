# Predict_Your_Next_Location_With_CNN

##  요약

######  홍대 근처에 나타난 위치데이터를 기반으로 사용자의 다음 위치를 예측합니다.
######  따라서 홍대를 벗어난 위치에 대해서는 결과값은 무의미합니다.
######  0.011(위도,경도 수치) 정도 정사각형의 맵 내에서만 위치 예측이 이루어집니다.

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
######  `templates/index.html` 의 다음 부분에 발급 받은 아이디를 입력합니다.
~~~xml
<script type="text/javascript" src="https://openapi.map.naver.com/openapi/v3/maps.js?ncpClientId=yourId"></script>
~~~

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
~~~
$ conda create --name env --file spec-file.txt
~~~

####  4. 설치한 가상환경 `env`로 이동합니다. 명령어는 다음과 같습니다.
~~~
conda activate env
~~~
######  만약 가상환경을 종료하려면
~~~
conda deactivate
~~~

####  5. `main.py` 가 있는 위치에서 다음 명령어를 입력합니다.
~~~
python3 main.py
~~~

####  6. 아래의 사진과 같은 메인 화면이 뜨면 `파일 선택` 버튼을 눌러서 1번에서 준비한 파일을 업로드합니다.

<img width="1680" alt="스크린샷 2020-02-15 오후 10 09 06" src="https://user-images.githubusercontent.com/48645552/74588445-d67e8900-503f-11ea-9e60-73f8c98942a3.png">

####  7. 결과화면 예시


