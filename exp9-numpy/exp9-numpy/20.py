import numpy as np

# Create a 3D array of shape (2, 3, 4)
arr = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:")
print(arr)

# Sum of all elements
total_sum = np.sum(arr)

# Sum of each layer
layer_sum = np.sum(arr, axis=(1, 2))

# Sum along rows
row_sum = np.sum(arr, axis=2)

# Sum along columns
column_sum = np.sum(arr, axis=1)

print("\nSum of all elements:")
print(total_sum)

print("\nSum of each layer:")
print(layer_sum)

print("\nSum along rows:")
print(row_sum)

print("\nSum along columns:")
print(column_sum)
