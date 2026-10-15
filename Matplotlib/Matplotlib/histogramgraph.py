import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 60, 65, 70, 70, 75, 80, 85, 90]

plt.hist(marks, bins=5)
plt.title("Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()