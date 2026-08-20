# Create a tuple of 10 numbers and display first five, last five, middle four, alternate and reverse tuple.numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print("First five elements:", numbers[:5])
print("Last five elements:", numbers[5:])
print("Middle four elements:", numbers[3:7])
print("Alternate elements:", numbers[::2])
print("Reverse tuple:", numbers[::-1])