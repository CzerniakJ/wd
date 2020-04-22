import numpy as np

def zad7(n):
    b = np.zeros((n,n))
    for x in range(n):
        for y in range(x):
            b[x,y] = (2+(2*x-2*y))
        for z in range(x):
            b[n-x-1,n-z-1] = (2+(2*x-2*z))
        b[x,x] = 2
    
    return b

print(zad7(5))