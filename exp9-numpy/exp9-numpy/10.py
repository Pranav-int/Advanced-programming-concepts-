import numpy as np

# Create a 4 x 4 matrix
matrix = np.array([
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

# Calculate row sums and column sums
row_sum = np.sum(matrix, axis=1)
column_sum = np.sum(matrix, axis=0)

print("Matrix:")
print(matrix)

print("\nSum of each row:")
print(row_sum)

print("\nSum of each column:")
print(column_sum)
