import numpy as np

# Create an array of 10 integers
arr = np.array([10, 25, 60, 45, 75, 30, 90, 15, 55, 40])

print("Original array:")
print(arr)

# Replace elements greater than 50 with 0
arr[arr > 50] = 0

print("\nArray after replacement:")
print(arr)
