def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    if((tmp := x1*w1 + x2*w2) <= theta):
        return 0
    else: return 1

if __name__=='__main__':
    x1, x2 = map(float, input("x1, x2 : ").split())
    print(AND(x1, x2))
