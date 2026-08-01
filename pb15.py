import numpy as np
"""
a=np.array([2,3,4,5])
b=np.array([6,7,8,9])

result=np.concatenate((a, b))
print(result)

#2d

c=np.array(
    [
        [1,2],
        [4,5]
    ]
)

d=np.array(
    [
        [7,8],
        [10,11]
    ]
)

result= np.concatenate((c, d),axis=1)
print(result)
result= np.concatenate((c, d),axis=0)
print(result)


result= np.vstack((c, d))
print(result)

array=np.array([1,2,3,4,5,6])
result=np.split(array,2)
print(result)

matrix=np.array([[1,2],[3,4],[5,6],[7,8]])
result=np.split(matrix,2)
print(result)

#multi dimention

matrix= np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix)

print(matrix.shape)#(3,3)

print(matrix.ndim)#2


print(matrix.size)#9

"""
#(height,width)->(n,1920,1080)

"""

array3=np.array([[[1,2],[2,4]],[[5,6],[7,8]]])
print(array3)

print(array3.shape)

"""
#(number of matrix, number of collum, number of row)
"""

array4=np.arange(12)
print(array4)

matrix=array4.reshape(3,4)
print(matrix)


"""
a=np.array([[5,6],[7,8]])
b=np.array([[9,10],[11,12]])

print(a+b)
print(a-b)
print(a*b)
print(a/b)


result=np.dot(a,b)
print(result)


#matrix transpose

print(a.T)

#matrix determinant
det=np.linalg.det(a)
print(det)

opposite=np.linalg.inv(a)
print(opposite)


#random number

random=np.random.rand(5) #0-1
print(random)

random=np.random.rand(3,3)
print(random)

random2=np.random.randint(1, 10,5)
print(random2)

random3=np.random.randint(1, 20,(3,4))
print(random3)

#produce same random result (seed)

np.random.seed(42)
random4=np.random.rand(5)
print(random4)

#choosing random number from arrays

array=np.array([10,20,30,40,50])
choice=np.random.choice(array)
print(choice)

choice=np.random.choice(array ,3)
print(choice)


