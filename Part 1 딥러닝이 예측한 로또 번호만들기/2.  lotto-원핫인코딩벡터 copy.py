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
