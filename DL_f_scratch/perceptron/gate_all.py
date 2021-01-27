import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])   #input
    w = np.array([0.5,0.5])   #weight
    b = -0.7   #bias
    if((tmp := np.sum(w*x) + b) <= 0): return 0
    else : return 1

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    if((tmp := np.sum(w*x) + b) <= 0): return 0
    else : return 1

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    if((tmp := np.sum(w*x) + b) <= 0): return 0
    else: return 1

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(x1, x2)
    return y



x1, x2 = map(float, input("x1, x2 : ").split())

print(f"{x1} AND {x2} = ",AND(x1, x2))
print(f"{x1} NAND {x2} = ",NAND(x1, x2))
print(f"{x1} OR {x2} = ", OR(x1, x2))
print(f"{x1} XOR {x2} = ", XOR(x1, x2))
