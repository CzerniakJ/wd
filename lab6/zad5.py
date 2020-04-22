import numpy as np

def zad5(n):
    a = np.arange(n,0,-1)
    b = np.zeros((n,n))
    for x in range(n):
        b[x,x] = a[x]
    return b
print(zad5(5))