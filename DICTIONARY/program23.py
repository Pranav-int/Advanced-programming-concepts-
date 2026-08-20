numbers = [1, 2, 2, 3, 1, 4, 2, 3]

frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

print(frequency)