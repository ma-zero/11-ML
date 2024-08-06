import matplotlib.pyplot as plt

x = [17,18,19,20,21,22,23]
y = [65,70,70,75,80,85,85]

plt.plot(x,y, marker='*', linestyle='--', color='red')
plt.title("Daily humidity trend")
plt.xlabel("Time (Hour)")
plt.ylabel("Humidity (%)")
plt.grid(True)
plt.show()
#plt.savefig("./linechart.png")