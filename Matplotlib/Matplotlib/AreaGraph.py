import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.fill_between(x, y)
plt.title("Area Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()