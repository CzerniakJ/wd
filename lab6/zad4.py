import numpy as np

def zad4(x, y):
    return np.logspace(1,y,y,base = x)
print(zad4(2,4))