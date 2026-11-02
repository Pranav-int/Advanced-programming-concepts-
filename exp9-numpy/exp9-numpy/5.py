import numpy as np

# Create a one-dimensional array containing numbers from 1 to 12
arr = np.arange(1, 13)

print("Original array:")
print(arr)

# Reshape into 2 x 6 matrix
matrix_2x6 = arr.reshape(2, 6)
print("\n2 x 6 Matrix:")
print(matrix_2x6)

# Reshape into 3 x 4 matrix
matrix_3x4 = arr.reshape(3, 4)
print("\n3 x 4 Matrix:")
print(matrix_3x4)

# Reshape into 4 x 3 matrix
matrix_4x3 = arr.reshape(4, 3)
print("\n4 x 3 Matrix:")
print(matrix_4x3)
