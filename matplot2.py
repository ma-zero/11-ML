import matplotlib.pyplot as plt

categories = ["Apple", "Banana", "Orange", "Strawberry", "Grape"]
values = [25, 30, 15, 20, 35]

plt.clf()
plt.bar(categories, values, color = 'skyblue')
plt.title("Fruit Sales")
plt.xlabel("Fruit")
plt.ylabel("Sales")

plt.show()
# plt.savefig("./bar.png)
# 실행 에러시 위에 드래그해서 ALT + Shift + E 눌러서 실행하면 됨