numbers=[1,2,3,4,5,6]
print(sum(numbers))
print(max(numbers))
print(min(numbers))

#abs()

x=-8
print(abs(x))

#round
y=3.52456
print(round(y))

#sorted
n=[8,4,6,1,9,0]
print(sorted(n))

#user defined func

def say_hello():
    print("hello")

say_hello()

#using single parameters

def say_hi(name):
    print(f"hii i am {name} ")

say_hi("sude")

#using multiple parameters

def say_hi(name,say_hi):
    print(name+ " "+say_hi)

say_hi("sude" ,"chatbox says hi to you")

#usege of return func

def sum(a,b):
    sum=a+b
    print(f"total: {sum}")
    return sum


sumation=sum(6,7)


print(f"sumation: {sumation}")

def calc(x,y):
    sum=x+y
    multi=x*y
    return sum,multi

calc_sum,calc_multi=calc(6,7)
print(f"sum: {calc_sum}")
print(f"multi:{calc_multi}")

def greating(name,message = "hello"):
    print(f"{name} {message}")

greating("sude","welcome")

def hi(name,age,job,c,lr,epoch):
    """
    Docstring

    """
    print(name,age,job,c,lr,epoch)

hi(name="sude",age="21",job="software eng",c="0.4",lr="0.001",epoch=1000)

#type hint

def sum(a:int,b:int)->int:
    return a+b


print(sum(6,7))

#nested func

def square(x):
    square=x**2
    return square

def output(x):
    print(square(x=4))


output(x)



