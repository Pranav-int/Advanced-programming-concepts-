import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 100]

plt.boxplot(marks)
plt.title("Box Plot")
plt.ylabel("Marks")
plt.show()