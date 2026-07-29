#1
with open("grade.txt","w",encoding="utf-8") as file:
    file.write("70\n")
    file.write("60\n")
    file.write("50\n")
    file.write("90\n")
    file.write("80\n")


#2

grade=[]

file = open("grade.txt","r",encoding="utf-8")
for line in file:
    grade.append(int(line.strip()))

print(f"{grade}")

highest=max(grade)
lowest=min(grade)
avarage=sum(grade)/len(grade)

print(f"\n{avarage}")
print(f"\n{lowest}")
print(f"\n{highest}")

#3


with open("results.txt","w",encoding="utf-8") as file:
    file.write(f"avarage: {int(avarage)}\n")
    if avarage>=50 :
        file.write("class passed!")
    else:
        file.write("class can't passed! ")
file.close()