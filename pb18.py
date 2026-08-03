import pandas as pd

data={"name":["Altay","Suha","Ozlem","Sude","Elif"],
      "Age":[22,53,53,21,21],
      "city":["Zonguldak","Izmir","Balikesir","Ayvalik","Izmir"],
      "Salary":[2000,3000,3000,4000,1000]}
df=pd.DataFrame(data)
print(df)

print(df["Age"])

print(df[["name","Salary"]])

print(df.iloc[0])

print(df.iloc[0:3])

print(df.loc[2])

print(df.loc[:,["name","Salary"]])

print(df.loc[:2,["name","Salary"]])

filter=df["Age"]>30
print(filter)

result=df[filter]
print(result)

print(df[df["Age"]<30],"\n")

result= df[(df["city"]=="Balikesir") &(df["Salary"]==3000)]
print(result)

print(df[df["city"]=="Istanbul"])

print(df[df["Age"]>25][["name","Salary"]])

data={"name":["Ali","Mehmet","Ayse"],
      "Age":[20 ,30, 40],
      "Salary": [3000,4000,5000]
      }
df=pd.DataFrame(data)
print(df)

df["city"]=["Famamagusta","Ankara","Istanbul"]
print(df,"\n")

df["Salary_year"]=df["Salary"]*12
print(df)

df=df.drop("Salary",axis=1)
print(df)

df=df.rename(columns={"Salary_year":"Salaryyear"})
print(df)

df.loc[3]=["Elif",21,"Ankara",30000]
print(df)

df=df.drop(0)
print(df)

df=df.reset_index(drop=True)
print(df)

data2={
    "name":["Ali","Ayse","Mehmet","Zeynep","Ahmet"],
    "city":["Balikesir","Ankara","Istanbul","Istanbul","Izmir"],
    "salary":[4000,3000,5000,8000,4500]
}
df=pd.DataFrame(data2)
print(df)

df_line=df.sort_values("salary",ascending=False)
print(df_line)

df_line=df.sort_values(["city","salary"])
print(df_line)

grups=df.groupby("city")
print(grups)

result=df.groupby("city")["salary"].mean()
print(result)

result=df.groupby("city")["salary"].sum()

result=df.groupby("city")["name"].count()
print(result)

result=df.groupby("city")["salary"].agg(["mean","max","min"])
print(result)

#pandas func()

data={"name":["Altay","Suha","Ozlem","Sude","Elif"],
      "Age":[22,53,53,21,21],
      "city":["Zonguldak","Izmir","Balikesir","Ayvalik","Izmir"],
      "Salary":[2000,3000,3000,4000,1000]}
df=pd.DataFrame(data)
print(df)


print(df.head(3))

print(df.tail(3))

print(df.info())

print(df.describe())

print(df["city"].value_counts())

print(df["city"].unique())

print(df["city"].nunique())

