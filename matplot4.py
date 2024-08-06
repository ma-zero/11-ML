# pie chart

import matplotlib.pyplot as plt

labels = ["English", "Math", "Science", "History"]
sizes = [45,30,15,10]

plt.clf()
plt.pie(sizes, labels=labels, autopct="%1.1f%%",
    startangle=140, colors=["lightblue", "lightgreen", "lightcoral", "lightsalmon"])

plt.title("Subjects Distribution")
plt.show()

# 대문자 소문자 구분해서 작성해야 작동함.