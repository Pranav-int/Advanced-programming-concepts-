import numpy as np

matrix1 = np.array([[1, 2, 3],[4, 5, 6]])

matrix2 = np.array([[7, 8],[9, 10],[11, 12]])


result = np.matmul(matrix1, matrix2)

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

print("\nMatrix Multiplication:")
print(result)
