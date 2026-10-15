import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.step(x, y)
plt.title("Step Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()