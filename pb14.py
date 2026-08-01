#indexin and slicing


import numpy as np
array=np.array([4,5,6,7,8])
print(array[2])

print(array[-2])

print(array[1:4]) #4th one is not including in numpy [5 6 7]

print(array[:3]) #[4 5 6]

print(array[2:]) #[5 6 7]

#stem usage 
print(array[::2]) #it goes 2 by 2

#2d indexing

matrix=np.array(
    [
        [1 ,2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)
print(matrix)

print(matrix[1, :])

print(matrix[: ,1])


print(matrix[0:2, 0:2])


matrix2= np.array(
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
)

print(matrix[2, :])
print(matrix[: ,2])
print(matrix[0:2, 0:2])