from __future__ import absolute_import, division, print_function, unicode_literals
# 딥러닝에 필요한 패키지를 설치해준다.
# !pip install tensorflow-gpu==2.0.0-rc1
# !pip install 'h5py==2.10.0' --force-reinstall

# 로토csv 파일을 넘파이 라이브러리를 활용해서 불러와 준다.
import numpy as np
rows = np.loadtxt("./Part 1 딥러닝이 예측한 로또 번호만들기/lotto.csv", delimiter=",")
row_count = len(rows)
print(row_count) # 로토csv이 1007이라는걸 알수 잇다.

# 당첨번호를 원핫인코딩백터(ohbin)으로 변환하기
def numbers2ohbin(numbers):
    ohbin = np.zeros(45) # 45개의 빈 칸을 만듬
    
    for i in range(6): # 6개의 당첨번호에 대해서 반복함
        ohbin[int(numbers[i])-1] = 1 #로또번호가 1부터 시작하지만 벡터의 인덱스 시작은 0부터 시작하므로 1을 뺌
        
    return ohbin
# 원핫인코딩벡터(ohbin)을 번호로 변환
def ohbin2numbers(ohbin):
    
    numbers = []
    
    for i in range(len(ohbin)):
        if ohbin[i] == 1.0: # 1,0으로 설정되어 있으면 해당 번호를 반환값에 추가한다.
            numbers.append(i+1)
    return numbers 

numbers = rows[:, 1:7]
ohbins = list(map(numbers2ohbin, numbers))

x_samples = ohbins[0:row_count-1]
y_samples = ohbins[1:row_count]

#원핫인코딩으로 표시
print("ohbins")
print("X[0]: " + str(x_samples[0]))
print("Y[0]: " + str(y_samples[0]))

#번호로 표시
print("numbers")
print("X[0]: " + str(ohbin2numbers(x_samples[0])))
print("Y[0]: " + str(ohbin2numbers(y_samples[0])))

# 훈련셋/검증셋/시험셋 분리
train_idx = (0,800)
val_idx = (801,900)
test_idx = (901,len(x_samples))

print(f"train:{train_idx}, val:{val_idx},test:{test_idx}")

# LSTM(RNN 계열) 모델

import tensorflow as tf
from tensorflow import keras
from tensorflow.python.keras import layers
from tensorflow.python.keras import models

# 모델을 정의합니다.
model = keras.Sequential([
    keras.layers.LSTM(128, batch_input_shape=(1, 1, 45), return_sequences=False, stateful=True),
    keras.layers.Dense(45, activation='sigmoid')
])

# 모델을 컴파일합니다.
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 매 에포크마다 훈련과 검증의 손실 및 정확도를 기록하기 위한 변수
train_loss = []
train_acc = []
val_loss = []
val_acc = []

# 최대 100번 에포크까지 수행
for epoch in range(100):

    model.reset_states() # 중요! 매 에포크마다 1회부터 다시 훈련하므로 상태 초기화 필요

    batch_train_loss = []
    batch_train_acc = []
    
    for i in range(train_idx[0], train_idx[1]):
        
        xs = x_samples[i].reshape(1, 1, 45)
        ys = y_samples[i].reshape(1, 45)
        
        loss, acc = model.train_on_batch(xs, ys) #배치만큼 모델에 학습시킴

        batch_train_loss.append(loss)
        batch_train_acc.append(acc)

    train_loss.append(np.mean(batch_train_loss))
    train_acc.append(np.mean(batch_train_acc))

    batch_val_loss = []
    batch_val_acc = []

    for i in range(val_idx[0], val_idx[1]):

        xs = x_samples[i].reshape(1, 1, 45)
        ys = y_samples[i].reshape(1, 45)
        
        loss, acc = model.test_on_batch(xs, ys) #배치만큼 모델에 입력하여 나온 답을 정답과 비교함
        
        batch_val_loss.append(loss)
        batch_val_acc.append(acc)

    val_loss.append(np.mean(batch_val_loss))
    val_acc.append(np.mean(batch_val_acc))

    print('epoch {0:4d} train acc {1:0.3f} loss {2:0.3f} val acc {3:0.3f} loss {4:0.3f}'.format(epoch, np.mean(batch_train_acc), np.mean(batch_train_loss), np.mean(batch_val_acc), np.mean(batch_val_loss)))