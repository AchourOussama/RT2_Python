import numpy as np
# a=np.arange(0,10,2)
# b=np.linspace(0,10,5)#deviding an interval into equal parts
# c=np.full(5,1.75)#full array of specified unique values
# print(c)
# print(b)
bigArray=np.arange(100,200,10)
#method1
array=np.resize(bigArray,(5,2))
#method2
array=np.reshape(bigArray,(5,2))
print(array)

