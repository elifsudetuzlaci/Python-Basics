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

