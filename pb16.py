#home work for numpy 
#1
"""
-crewate a number with numbers 1 to 20 with numpy 

"""
import numpy as np

a=np.arange(1,21)
print(a)
print("size: ",a.size)

#2
"""
-create numpy array 5 to 25 5 by 5
"""
b=np.arange(5,30,5)
print(b)
result=b*3
print(result)

#3
"""
-array 0-30
-slicing between 10-20
"""
c=np.arange(0,31)
print(c)
print(c[10: 21])

#4
a=np.array([1,2,3])
b=np.array([4,5,6])
result=np.concatenate((a,b))
print(result)

#5
d=np.arange(1,13)
matrix= d.reshape(3,4)
print(matrix)
print(matrix.shape)

#6
matrix2=np.array([[1,2,3],[4,5,6],[7,8,9]])

print("second collum:", matrix2[1])
print("second row: ", matrix2[:,1]) 

#7
random=np.random.rand(3,3)
print(random)
print(random.mean())
print(np.max(random))

#8
a=np.array([2,4,6,8])
b=np.array([1,3,5,7])
multiplying=a*b
print(multiplying)

#9
array=np.arange(1,10)
matrix3=array.reshape(3,3)
print(matrix3)
print(matrix3.T)

#10
numbers=np.random.randint(1,51,10)
print(numbers)
print(np.sum(numbers))
print(np.mean(numbers))