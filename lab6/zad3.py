import numpy as np

def zad3(n):
    b = np.arange(1,(n*n)+1,1).reshape(n,n)
    return b

print(zad3(5))