import numpy as np

# Create an unsorted array
arr = np.array([45, 12, 78, 3, 56, 23, 89, 10])

# Ascending order
ascending = np.sort(arr)

# Descending order
descending = np.sort(arr)[::-1]

print("Original array:")
print(arr)

print("\nAscending order:")
print(ascending)

print("\nDescending order:")
print(descending)
