#file

file=open("test.txt","r", encoding="utf-8")
context= file.read()
print(context)
file.close()


#reading line by line

file=open("test.txt","r", encoding="utf-8")
for line in file:
    print(line.strip())

file.close()


file=open("test.txt","r", encoding="utf-8")
context=file.read()
file.close()

print(context)
new_context=context.upper()
print(f"new_context: \n{new_context}")

#count of line 
file=open("test.txt","r",encoding="utf-8")
line=file.readlines()
file.close()

print(f"all lines: \n{len(line)}")

file=open("new-file.txt","w",encoding="utf-8")
file.write("hello")
file.write("\nI am Sude")
file.close()


file=open("test.txt","r",encoding="utf-8")
context=file.read()
file.close()
new_file=context.upper()

file=open("new_test.txt","w",encoding="utf-8")
file.write(new_context)
file.close()


with open("test.txt","r",encoding="utf-8") as file:
    context=file.read()
    print("with ")
    print(context)

