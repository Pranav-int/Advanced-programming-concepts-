import numpy as np

# Create an array from 1 to 20
arr = np.arange(1, 21)

print("Original array:")
print(arr)

# First 5 elements
print("\nFirst 5 elements:")
print(arr[:5])

# Last 5 elements
print("\nLast 5 elements:")
print(arr[-5:])

# Alternate elements
print("\nAlternate elements:")
print(arr[::2])

# Elements in reverse order
print("\nReverse order:")
print(arr[::-1])
