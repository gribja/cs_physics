# lagrange's interpolation

import numpy as np

xs = np.random.randint(low=1, high=50, size=5)
ys = np.random.randint(low=1, high=50, size=5)

def lagrunge(x,xp,yp):
    if len(xp)==len(yp):
        n = len(xp)
        arr = np.zeros((2,n))
        arr[0],arr[1] = xp,yp
    else:
        print("You think you can trick me? Huh!!")

    res = 0
    for i in range(0,n):
        temp = arr[1][i]
        for j in range(0,n):
            if j!=i:
                temp *= (x - arr[0][j])/(arr[0][i] - arr[0][j])
        res += temp
    return res

print(xs)
print(ys)
print(lagrunge(3,xs,ys))

        
