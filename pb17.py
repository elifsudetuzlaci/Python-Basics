import pandas as pd
#series

data=pd.Series([10,20,30,40])
print(data) 

"""
index  value
0       10
1       20
2       30
3       40
dtype: int64
"""

data=pd.Series([10,20,30])
print(data[0]) #10

data= pd.Series([10,20,30],index=["a","b","c",])
print(data)

print(data["b"])

data2={"ali":90,"ayse":65,"fatma":70}
s=pd.Series(data2)
print(s)


print(s.index)
print(s.values)
print(s.dtype)

data3=pd.Series([10,20,30,40])
result=data3*2
print(result)

age=pd.Series([10,20,30,40,50])
filter=age>25#boolean filter
print(filter)

result=age[filter]
print(result)

#dataframe

data={"name":["Alex","Sue","Carl"],
      "age":[25,30,35],
      "city":["stockholm","Paris","London"]}

df=pd.DataFrame(data)
print(df)


print(df.columns)
print(df.shape)

print(df["name"])

print(df[["name","age"]])

df["salary"]=[5000,6000,7000]
print(df)

df=df.drop("city",axis=1)
print(df)

print(df.head())#first 5 row

print(df.tail())

print(df.info())


#csv file reading
df=pd.read_csv("data.csv")
print(df)

df=pd.read_excel("data_excel.xlsx")
print(df)

#writing csv file
data={"name":["Mustafa","Kemal","Altay"],"age":[38,40,22]}

df=pd.DataFrame(data)
df.to_csv("data2.csv",index=False)

df={"name":["Alex","Sue","Carl"],
      "age":[25,30,35],
      "city":["stockholm","Paris","London"]}

df=pd.DataFrame(data)
df.to_excel("data_excel2.xlsx",index=False)


