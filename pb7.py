#scoping

#local
def test():
    x=10
    print(f"inside of function: {x}")

test()

#global
x=15
def test2():
    print(x)

test2()

x=11
def test3():
    x=5
    print(f"inside of function: {x}")

test3()
print(f"out side of funcÇ: {x}")


#global key
x=9
def test4():
    global x
    x=3
test4()
print(x)


#project about func()

def avarage(midterm:float,final:float)->float:
    avarage =midterm*0.4+final*0.6
    return avarage



def letter(avarage:float)->str:
    if avarage>=85:
        return "A"
    elif avarage>=70:
        return "B"
    elif avarage>=60:
        return "c"
    elif avarage>=50:
        return "D"
    else:
        return "F"
        




def output_of_results(name:str,avarage:float,letter:str):
    print("----results----")
    print(f"student",{name})
    print(f"Average: {avarage}")
    print(f"Letter grade: {letter}")

name=input("name: ")
midterm=float(input("midterm grade: "))
final=float(input("final grade: "))

avarage=avarage(midterm=midterm,final=final)

letter=letter(avareage=avarage)

output_of_results(name=name,average=avarage,letter=letter)

