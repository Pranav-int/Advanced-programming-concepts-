import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.stem(x, y)
plt.title("Stem Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()