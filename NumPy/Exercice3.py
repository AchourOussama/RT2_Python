from random import randint
import numpy as np
arrayOne=np.array([[randint(0,10) for i in range(3)] for j in range(3)])
arrayTwo=np.array([[randint(0,10) for i in range(3)] for j in range(3)])
arrayResult=arrayOne+arrayTwo
print('array one:\n{}\narray two:\n{}'.format(arrayOne,arrayTwo))
print('array Result (sum):\n',arrayResult)
arrayResult=np.array(list(map(lambda x:x**2,arrayResult)))

print('array Result (with squares) :\n',arrayResult)