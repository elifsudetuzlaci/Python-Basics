#homework for matplotlib


import matplotlib.pyplot as plt

months=["january","feb","march","april","may","june"]
sales=[120,150,170,160,200,220]
profits=[20,35,40,30,50,60]
adv=[5,8,10,12,15,18]

plt.plot(months,sales)
plt.xlabel("months")
plt.ylabel("sales")
plt.show()

plt.plot(months,profits,color="red")
plt.xlabel("months")
plt.ylabel("profits")
plt.show()

plt.plot(months,sales,marker="o")
plt.xlabel("months")
plt.ylabel("sales")
plt.show()


plt.bar(months,sales)
plt.xlabel("months")
plt.ylabel("sales")
plt.show()

plt.bar(months,sales,color="green")
plt.xlabel("months")
plt.ylabel("sales")
plt.show()

colors=["red","blue","purple","green","grey","pink"]
plt.pie(sales,labels=months,autopct="%1.1f%%",colors=colors)
plt.axis("equal")
plt.show()

plt.scatter(adv,sales,color="red",s=100)
plt.xlabel("advertisement")
plt.ylabel("sales")
plt.show()

import matplotlib.pyplot as plt
months=["january","feb","march","april","may","june"]
sales=[120,150,170,160,200,220]
profits=[20,35,40,30,50,60]
adv=[5,8,10,12,15,18]

plt.subplot(1,2,1)
plt.plot(months, sales,marker="o")
plt.title("sales")

plt.subplot(1,2,2)
plt.bar(months,profits,color="orange")
plt.title("profits")

plt.show()

#----------------------------------------------------------------------------------------------------------------------------------------------

plt.subplot(2,2,1)
plt.plot(months,sales,marker="o")
plt.title("sales")

plt.subplot(2,2,2)
plt.bar(months,profits,color="green")
plt.title("profits")

plt.subplot(2,2,3)
plt.scatter(adv,sales,color="purple",s=100)
plt.title("advertisement-sales")

plt.subplot(2,2,4)
plt.pie(sales,labels=months,autopct="%1.1f%%",colors=colors)
plt.title("sales")

plt.show()