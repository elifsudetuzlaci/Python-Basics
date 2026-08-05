#matplotlib library
"""
data virtualization
"""
import matplotlib.pyplot as plt

days=[1,2,3,4,5,6,7]
heat=[34,35,33,34,37,40,37]
"""
#line plot
plt.plot(days,heat,color="purple",linestyle="--",marker="o")#(x,y)
plt.title("weather")#head of graphics 
plt.xlabel("days")
plt.ylabel("heat")
plt.grid(True)
plt.show()
"""
"""
import matplotlib.pyplot as plt
#bar chart
name=["Sude","Altay","Elif","Ozlem","Suha"]
grades=[100,70,45,80,90]
colors=["red","blue","pink","purple","green"]
plt.bar(name,grades,color=colors)
plt.xlabel("name")
plt.ylabel("grades")
plt.title("school grades")
plt.show()

plt.barh(name,grades,color=colors)
plt.show()
"""

#pie chart
import matplotlib.pyplot as plt
label=["python","c","java","sql","ruby"]
values=[40,5,10,20,25]
colors=["red","blue","purple","green","grey"]
a=[0 ,0.1 ,0, 0,0.2]
plt.pie(values,labels=label,explode=a,autopct="%1.1f%%",colors=colors)
plt.title("coding languages")
plt.show()


import matplotlib.pyplot as plt
working_hour=[5,6,7,8,7]
grades=[50,60,50,80,100]

plt.scatter(working_hour,grades,color="red",s=100)
plt.title("working hours and grades")
plt.xlabel("working hour")
plt.ylabel("grades")
plt.show()

x1=[1,2,3,4]
y1=[50,70,80,100]

x2=[1,2,3,4]
y2=[75,85,90,100]

plt.scatter(x1,x2,color="blue",label="science")
plt.scatter(y1,y2,color="red",label="math")
plt.legend()
plt.show()

import matplotlib.pyplot as plt

x=[1,2,3,4]
y1=[10,20,30,40]
y2=[40,30,20,10]

plt.subplot(1,2,1)
plt.plot(x,y1)
plt.title("graph 1")


plt.subplot(1,2,2)
plt.plot(x,y2)
plt.title("graph 2")

plt.show()

x=[1,2,3,4]
y=[10,20,30,40]

plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("line plot")

plt.subplot(1,2,2)
plt.bar(x,y)
plt.title("bar plot")
plt.show()


x=[1,2,3,4]
y=[10,20,30,40]

plt.subplot(2,2,1)
plt.plot(x,y)
plt.title("graphic 1")

plt.subplot(2,2,2)
plt.bar(x,y)
plt.title("graphic 2")

plt.subplot(2,2,3)
plt.scatter(x,y)
plt.title("graphic 3")

plt.subplot(2,2,4)
plt.pie(y)
plt.title("graphic 4")

plt.show()


