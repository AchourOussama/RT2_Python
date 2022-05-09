import numpy as np
array=np.reshape(np.arange(10,34,1),(8,3))
subArrays=np.split(array,4)
print("Big Array:\n\n",array,end='\n\n')

for i in range(4):
    print("sub array n°{}:\n\n{}\n".format(i+1,subArrays[i]))