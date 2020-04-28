import numpy as np
a = np.arange(11,20,1).reshape((3,3))
for i in a.flat:
    print(i)