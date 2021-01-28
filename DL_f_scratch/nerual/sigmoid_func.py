#시그모이드 함수 구현
#함수가 numpy 배열을 처리할 수 잇는 이유 : 브로드캐스트 -> numpy 배열과 스칼라값의 연산을 numpy 배열의 원소 각각과 스칼라값의 연산으로 바꿔 수행

import numpy as np
import matplotlib.pylab as plt

import matplotlib
matplotlib.use('TkAgg')


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1, 1)
plt.show()
