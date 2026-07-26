#sets

numbers={1,2,3,4}
print(numbers)

#sets are work with uniqeu data if it has 2 2 one of the 2 print as set 
numbers={1,2,2,3,3,3,4,4}
print(numbers)

#don't have index

list=[1,2,3,4,4,4,2,3,2]
unique=set(list)
print(unique)

a={1,2,3}
b={3,4,5}

print(a.union(b))

print(a.intersection(b))

print(a.difference(b))


age= input("age:")

print(int(age))


price=input("price: ")
print(float(price))

sum= float(price) + (float(price)*18 /100)

print("sum:", int(sum))


#3

numbers=[10,20,30,40,50]
print(list[0])
print(list[-1])
print(list[1:])
numbers.append(60)
print(list)
numbers.remove(20)
print(numbers)

#4

tup=(12,34)
x,y=tup

print(x)
print(y)

#
#numbers=(1,2,3,4,5,6)
#numbers.append(8)
#print(numbers)


#5

dict={"name":"Sude","Age":21,"department":"software"}

print(dict["name"])
dict["not"]=90
dict["Age"]=22

print(dict)

#6
names=["Altay","Ozlem","sude","suha"]
unique_names=set(names)
print(unique_names)
print(len(unique_names))
