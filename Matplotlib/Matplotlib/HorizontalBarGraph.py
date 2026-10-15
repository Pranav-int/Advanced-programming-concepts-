import matplotlib.pyplot as plt

students = ["A", "B", "C", "D"]
marks = [80, 70, 90, 60]

plt.barh(students, marks)
plt.title("Horizontal Bar Graph")
plt.xlabel("Marks")
plt.ylabel("Students")
plt.show()