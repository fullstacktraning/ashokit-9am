import matplotlib.pyplot as plt
import pandas as pd

# x = [1,2,3,4]
# y = [10,20,15,25]
# df = pd.read_csv("graphs.csv")
# x = df["x"]
# y = df["y"]
# # plt.plot(x,y)
# # plt.plot(x,y,color='red')
# plt.plot(x,y,color='orange',linestyle=':',marker='x') # linestyles = "-", "--", ":"  marker = "o","x", "*"
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")
# plt.title("Line Plot")
# plt.show()

x = ["std1","std2","std3","std4","std5"]
y = [60,70,80,90,100]
bars = plt.bar(x,y,color=['red','green','blue'],width=0.5,edgecolor='black')
for bar in bars:
    plt.text(-0.25 + bar.get_x() + bar.get_width()/2, bar.get_height(), bar.get_height(), ha="center",va="center")

#plt.barh(x,y)
plt.title("Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
