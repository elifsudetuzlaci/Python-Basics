grades =[]
error_count=0




with open("grades.txt","r",encoding="utf-8") as file:
    for line in file:
        try:
            grade_value=int(line.strip())
            grades.append(grade_value)
        except ValueError:
            print(f"data error: {line.strip()}")
            error_count +=1
            print(f"{error_count}")


avarage= sum(grades)/len(grades)
print(f"{avarage}")