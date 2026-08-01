#numpy library

import numpy as np

numbers = np.array([1, 2, 3, 4, 5])

print(numbers)
print(numbers.mean())

"""
arrays

-ndarray: n dimantional arrays 
-
"""

#list vs array
number=[1,2,3,4,5,6]#list
print(number)

array=np.array(number)
print(number)

print(type(array))


print(array.shape)

print(array.dtype)


array=np.zeros(5)
print(array)

array=np.ones(5)
print(array)

array=np.arange(0,10)
print(array)

array=np.arange(0,10,2)
print(array)

array=np.linspace(0,10,5)
print(array)

