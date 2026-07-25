#tuples -> ()

koordinat=(10,20)
renkler= ("kirmizi","mavi","green")

#tuples are inmuteable that s why you can't change it

t=(10,20,30,40)
print(t[1])
print(t[-1])

print(t[1:3])


#if tuple has onle one data when you pint it its just a int,float or char
 
#it s tuple when you add , comma oparetor 
x=(5,)
print(type(x))


#tuple unpacking 
koordinat=(10,20)
x,y=koordinat
print(x)
print(y)

t=(20,20,30,40)
print(t.count(20))
print(t.index(30))



#Dictionary
student={

    "isim":"ali",
    "age":25,
    "department":"computer"
}

print(student["isim"])

#update the data

student["age"]=26
print(student)


#deletint data from dict

del student["department"]

print(student)

print(student.keys())
print(student.values())
print(student.items())
