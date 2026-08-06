#object orianted programming 

class student:

    def __init__(self,name,age):
        print(f"new student! : name: {name}, age:{age}")


studen1=student("Altay",22)


"""
attribute is a structure that keeps datas for objects 
"""

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age


student1=student("Altay",22)

print(student1.name)
print(student1.age)


class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def introduce(self):
        print(f"hello my name is: {self.name},{self.age}")


student1=student("Altay",22)
student2=student("Elif",22)

student1.introduce()
student2.introduce()



class book:
    def __init__(self,name,writer,page):
        self.name=name
        self.writer=writer
        self.page=page

    def info(self):
        print(f"Book: {self.name}" )
        print(f"Writer: {self.writer}")
        print(f"Number of page: {self.page}")

book1=book("the call of the wild ","Jack London",250)
print(book1.name)
print(book1.writer)
print(book1.page)


book1.info()


book1=book("the call of the wild ","Jack London",250)
book2=book("Harry Potter ","j.k rowling",500)
book3=book("utopia ","Thomas more",300)

print(book2.name)
book3.info()

