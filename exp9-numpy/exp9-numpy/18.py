import numpy as np

# Create a 3D array of shape (2, 3, 4)
arr = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:")
print(arr)

print("\nNumber of dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)
