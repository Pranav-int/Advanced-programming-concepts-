import numpy as np

# Create two 3 x 3 matrices
matrix1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

matrix2 = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

# Perform matrix addition
result = matrix1 + matrix2

# Display the matrices and result
print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

print("\nMatrix Addition:")
print(result)
