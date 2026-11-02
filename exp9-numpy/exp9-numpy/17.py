import numpy as np

# Marks of 20 students
marks = np.array([
    65, 78, 82, 91, 56,
    73, 88, 95, 67, 84,
    76, 89, 92, 61, 70,
    85, 79, 93, 68, 87
])

# Calculate class average
average = np.mean(marks)

# Select marks above average using Boolean indexing
above_average = marks[marks > average]

print("Marks of 20 students:")
print(marks)

print("\nClass average:", average)

print("\nStudents who scored above average:")
print(above_average)
