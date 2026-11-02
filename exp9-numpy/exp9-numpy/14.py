import numpy as np

# Create an array containing duplicate values
arr = np.array([10, 20, 10, 30, 20, 40, 30, 50, 40, 10])

# Find unique elements
unique_elements = np.unique(arr)

print("Original array:")
print(arr)

print("\nUnique elements:")
print(unique_elements)
