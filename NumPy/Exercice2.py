from ctypes import Array
from random import randint, random
import re
import numpy as np
array=np.array([[randint(0,10) for i in range(3)] for j in range(3)])
# print(type(np.shape(array)))
print(array)
def extractColomn(a:np.ndarray):
    ls=[]
    for i in range(np.shape(a)[0]):
        ls.append(a[i][len(a[i])-1])
        #or we can use again the np.shape() method
        
        # ls.append(a[i][np.shape(a)[1]-1])
    return ls

print(extractColomn(array))



