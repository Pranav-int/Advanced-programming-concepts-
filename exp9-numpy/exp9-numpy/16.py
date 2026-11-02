import numpy as np

# Marks of 10 students
marks = np.array([78, 85, 92, 67, 74, 88, 95, 81, 69, 90])

print("Marks:", marks)

# Calculate statistics
print("Highest marks:", np.max(marks))
print("Lowest marks:", np.min(marks))
print("Average marks:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard deviation:", np.std(marks))
