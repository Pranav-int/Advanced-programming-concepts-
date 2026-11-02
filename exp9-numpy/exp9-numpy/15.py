import numpy as np

# Create two arrays
arr1 = np.array([[1, 2, 3],
                 [4, 5, 6]])

arr2 = np.array([[7, 8, 9],
                 [10, 11, 12]])

# Horizontal concatenation
horizontal = np.hstack((arr1, arr2))

# Vertical concatenation
vertical = np.vstack((arr1, arr2))

print("Array 1:")
print(arr1)

print("\nArray 2:")
print(arr2)

print("\nHorizontal concatenation:")
print(horizontal)

print("\nVertical concatenation:")
print(vertical)
