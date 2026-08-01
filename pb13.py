#math with numpy
import numpy as np

#add
a=np.array([1,2,3])
b=np.array([4,5,6])
result=a+b
print(result)

result=a-b
print(result)

#multiply

result=a*b
print(result)

#division
result=a/b
print(result)

a=np.array([1,2,3,4])
result=a*2
print(result)

result=a**2
print(result)

result=a**1/2
print(result)
result=np.sqrt(a)
print(result)

b=np.array([1,2,3,4,5])
print(np.sum(b))

print(np.mean(b))
print(np.max(b))
print(np.min(b))


print(np.std(b))