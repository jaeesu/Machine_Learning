#계단함수 구현

def step_function(x):
    if x>0: return 1
    else: return 0

#x는 실수(부동소수점)만 받아들인다. -> numpy 배열을 인수로 넣을 수 없다.
'''
import numpy as np

def step_function(x):
    y = x > 0
    return y.astype(np.int)

x = np.array([-1.0, 1.0, 2.0])
print(x)
y = x>0
print(y)
#array([False, True, True],dtype = bool)
y = y.astype(np.int)
print(y)
array([0,1,1])

    '''
