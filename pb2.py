#Lists

numbers=[1,2,3,4,5,6,7,8,9]
names=["altay","sude","ozlem"]

#list index
fruits=["elma","kiraz","kavun"]

print(fruits[0])

#list length

print(len(fruits))

#slicing

numbers=[1,2,3,4,5,6,7,8,9]
print(numbers[2:4]) #first inclusive second part exculusive

print(numbers[:3])

#adding new data in lists
numbers=[1,2,3]
numbers.append(4)
print(numbers)  

numbers.insert(1,100)
print(numbers)

numbers.remove(100)
print(numbers)

numbers.pop()
print(numbers)

numbers.pop(0)
print(numbers)
numbers[0]=999
print(numbers)
