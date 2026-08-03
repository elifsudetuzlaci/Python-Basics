#questions about pandas from tyza

import pandas as pd

data={"name":["Altay","Suha","Ozlem","Sude","Elif","Ece"],
      "Age":[22,53,53,21,21,23],
      "city":["Zonguldak","Izmir","Balikesir","Ayvalik","Izmir","Balikesir"],
      "Salary":[2000,3000,3000,7000,1000,40000]}
df=pd.DataFrame(data)
print(df)
print("-"*50)

#1
print(df.head(3),"\n")

#2
print(df.columns,"\n")

#3
print(df["name"],"\n")

#4
print(df[["name","Salary"]],"\n")

#5
filter=df["Age"]>28
print(filter)

#6
print(df[df["Salary"]>6000][["name","Salary"]])

#7
df_line=df.sort_values("Salary")
print(df_line)


#8
df_line=df.sort_values("Salary",ascending=False)
print(df_line)

#9
print(df.groupby("city")["Salary"].mean())

print("-"*50)

#10

df["year_salary"]=df["Salary"]*12

print(df)

df=df.drop("Salary",axis=1)
print(df)
