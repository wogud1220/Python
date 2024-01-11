# 사용자로부터 나이대, 성별을 입력받아서
# 가장 관심이 있을 상품 분류를 출력하는 프로그램을 작성

# 10대 남성: 만화
# 10대 여성: 화장품
# 20대 남성: 게임
# 20대 여성: 의류
# 30대 남성: 건강식품
# 30대 여성: 애완동물 관ㄹ녀
# 40대 남성: 자전거
# 40대 여성: 골프
# 50대 남성: 낚시
# 50대 여성: 수험생

import tensorflow as tf
from tensorflow import keras
import numpy as np
from keras.models import Sequential

#내부 신경망을 구성할 레이어들을 로딩한다.
from keras.layers import Conv1D, MaxPooling1D, Flatten, Dense

interest = {
    0: "만화",
    1: "화장품",
    2: "게임",
    3: "의류",
    4: "건강식품",
    5: "애완동물",
    6: "자전거",
    7: "골프",
    8: "낚시",
    9: "수험생"
}




#입력
age=input('나이대를 입력하세요:')
gender=input('성별을 입력하세요 남자: 1, 여자: 2')
human=age+gender


model=Sequential()
model.add(Dense(10, activation='relu', input_shape=(2,)))
model.add(Dense(len(interest), activation='softmax'))

model.compile(optimizer='adam', lose='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(features, labels, batch_size=32, epochs=300)

age=int(input('나이대를 입력하세요:'))
gender=int(input('성별을 입력하세요 남자: 1, 여자: 2'))