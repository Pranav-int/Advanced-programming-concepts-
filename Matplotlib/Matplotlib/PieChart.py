import matplotlib.pyplot as plt

subjects = ["Python", "Java", "SQL", "HTML"]
marks = [30, 25, 20, 25]

plt.pie(marks, labels=subjects, autopct="%1.1f%%")
plt.title("Pie Chart")
plt.show()