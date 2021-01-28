#plt -> 계단함수

import numpy as np
import matplotlib.pylab as plt

import matplotlib
matplotlib.use('TkAgg')

def step_function(x):
    return np.array(x>0, dtype=np.int)

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
