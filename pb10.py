#error managment
"""
-try -except


"""
try:
    number=int(input("Enter number: "))
    print(10/number)
except:
    print("error")

print("it continuos succesfully")


try:
    number=int(input("enter number: "))
    print(10/number)
except ValueError:
    print("please enter a number")
except ZeroDivisionError:
    print("cant diveded by 0")
        



try:
    number= int(input("please enter: "))
    result=10/number
except (ValueError,ZeroDivisionError):
    print("error:")
else: 
    print(f"result: {result}")

try: 
    file= open("data.txt","r",encoding="utf-8")
    content=file.read()
    print(content)

except FileNotFoundError:
    print("file couldnt found")
finally:
    try:
        file.close()
    except:
        pass



age= int(input("age: "))
if age<0:
    raise ValueError("ages cant be negative. ")


try: 
    n= int(input("number: "))
    print(10/n)
except Exception as e:
    print(f"hata: {str(e)}")



