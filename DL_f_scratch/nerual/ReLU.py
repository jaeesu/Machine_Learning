#ReLU : Recified Linear Unit

#임계치를 지나면 그 입력을 그대로 출력, 임계치 이하면 0을 출력

import numpy as np

def relu(x):
    return np.maximum(0,x)   # 두 입력 중 큰 값을 반환


#np.ndim : 배열의 차원 수
#np.shape : 배열의 형상 -> tuple
#np.dot : 1.벡터, 2.행렬의 곱
#행렬의 형상이 다를 경우 오류

#편향, 활성화 함수 생략, 가중치만 갖는 신경망
#편향은 오른쪽 아래 인덱스가 하나밖에 없다.

#3층 신경망

x = np.array([1.0, 0.5])
w1 = np.array([0.1, 0.3, 0.5], [0.2, 0.4, 0.6])
b1 = np.array([0.1, 0.2, 0.3])

print(w1.shape)
print(x.shape)
print(b1.shape)

a1 = np.dot(x, w1) + b1

#활성화 함수로 sigmoid 함수 사용
z1 = sigmoid(a1)

print(a1)
print(z1)
