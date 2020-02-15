import flask
import numpy as np
from scipy import misc
from tensorflow.keras.models import load_model
from tensorflow.keras import backend as K
import json
import os
from flask import Flask, flash, request, redirect, url_for ,render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './temfile'
ALLOWED_EXTENSIONS = {'json'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# 메인 페이지 라우팅
@app.route("/")
@app.route("/index")
def index():
    return flask.render_template('index.html')


# 데이터 예측 처리
@app.route('/predict', methods=['POST'])
def make_prediction():
    if request.method == 'POST':
        basePoint = [126.916810,37.548029]
        squareSize=0.011
        img_rows, img_cols = 24, 24
        input_shape=(24,24,1)
        pNum=10
        # 업로드 파일 처리 분기
        if 'jsData' not in request.files:
            return render_template('index.html', label="No1 Files")
        file = request.files['jsData']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return render_template('index.html', label="No2 Files")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        with open('./temfile/{}'.format(filename), encoding='UTF8') as f:
            data = json.loads(f.read())


        # 24*24 중 1개의 타일 변의 크기
        dl = squareSize / img_rows

        # basePoint 사각형 내에 있는 데이터만 거르기
        verifyJsonData=list()
        for x in data:
            if basePoint[0]<= float(x['longitude']) <basePoint[0]+squareSize:
                if basePoint[1] <= float(x['latitude']) < basePoint[1]+squareSize:
                    verifyJsonData.append(x)

        # 최신순 으로부터 pNum개를 뽑기 위해 뒤집습니다.
        verifyJsonData=verifyJsonData[::-1]

        # 검증된 데이터셋을 [x좌표,y좌표,번호] 형식으로 만들기
        tmpmap = [ [0 for _ in range(img_rows)] for _ in range(img_rows)]
        # 위도 경로를 저장하기 위한 배열을 선언합니다.
        trajectory = list()
        # pNum개 보다 많으면 루프문을 탈출합니다.
        cnt=0

        for x in verifyJsonData:
            trajectory.append([float(x['latitude']),float(x['longitude'])])
            cnt+=1
            idx,idy=0,0
            for _idx in range(1,img_rows+1):
                if basePoint[0]+_idx*dl > float(x['longitude']):
                    idx = _idx-1
                    break
            for _idy in range(1,img_rows+1):
                if basePoint[1]+_idy*dl > float(x['latitude']):
                    idy = _idy-1
                    break
            tmpmap[idx][idy]+=1
            if cnt >=pNum:
                break

        x_test=list()
        x_test.append(tmpmap)
        x_test = np.array(x_test)
        #혹시 케라스 이미지 포멧이 채널이 first인경우는 바꿔준다
        if K.image_data_format() == 'channels_first':
            x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
            input_shape = (1, img_rows, img_cols)
        else:
            x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
            input_shape = (img_rows, img_cols, 1)
        x_test = x_test.astype('float32')
        x_test /= pNum

        model = load_model('keraslocationpredict.h5')
        y = model.predict_classes(x_test)
        K.clear_session()
        longitude = y%img_rows
        latitude = y/img_cols

        longitude = longitude*dl + basePoint[0]
        latitude = latitude*dl + basePoint[1]

        longitude = longitude[0]
        latitude = latitude[0]

        dlon = longitude + dl
        dlat = latitude + dl
        # 결과 리턴
        return render_template('index.html', latitude=latitude,longitude=longitude,dlon=dlon,dlat=dlat,trajectory=trajectory)


if __name__ == '__main__':
    # 모델 로드
    # ml/model.py 선 실행 후 생성
    # Flask 서비스 스타트
    app.run(host='0.0.0.0', port=8000, debug=True)
