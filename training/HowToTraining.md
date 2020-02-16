#	How To Training

### 1. 모델 설명

#### 1-1. 데이터 전처리

######  먼저 지도의 영역을 설정합니다. 지도의 영역을 정사각형 모양으로 하고 정사각형의 왼쪽의 하단 점을 `basePoint` 라고 지정합니다. 예시로 아래의 그림에서 홍대의 일정 영역을 자릅니다. ( 아래는 예시이며 실제 구현은 24*24 이며 pNum=10 으로 했습니다 )

<img width="909" alt="스크린샷 2020-02-16 오후 4 35 58" src="https://user-images.githubusercontent.com/48645552/74600879-c962a800-50da-11ea-9eb2-f584a858cac4.png">


######  다음으로 `pNum` 을 정의 합니다. `pNum` 은 훈련 데이터에서 패턴 개수를 의미합니다. 예를 들어 (0,1,2,3,4) 이라는 경로가 있고 `pNum = 2` 라면 훈련데이터는 (0,1),(1,2),(2,3) 으로 정의되고 label의 값은 각각 (2,3,4) 가 됩니다. 예를 들어 위의 그림을 참조 했을 때, 나의 json data의 경로가  `0,1,1,6,11` 이고 `pNum = 3` 이라면 train set은 다음과 같이 만들어집니다.
~~~python
x_train=[
  [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [1,2,0,0]
  ],
  [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,1,0],
    [0,2,0,0]
  ]
]
y_train=[6,11]
~~~

####  1-2. keras 모델

######  Model : `CNN`

######  Architecture : `Cov(5*5) - MaxPool(2*2)  - Cov(5*5)  - MaxPool(2*2)  - FFN(576)`
######  자세한 사항은 코드를 참조하세요.


### 2. 훈련 사용 방법

파일명 | 설명
:---: | :---:
`training/data/trainData.json`  | 모델을 학습하기 위해 `gpx`파일을 `json`으로 파싱한 것입니다.
`training/data/testData.json` | 모델을 테스트 하기 위해 사용한 `json` 파일입니다.
`training/training.ipynb`  | 모델을 학습 시킵니다. 모델은 `keraslocationpredict.h5`로 저장됩니다.
`training/test.ipynb` | 모델을 테스트 할 수 있습니다.
