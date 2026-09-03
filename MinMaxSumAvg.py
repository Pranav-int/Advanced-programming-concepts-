def calculate(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    return minimum, maximum, total, average



numbers = [10, 20, 30, 40, 50]

result = calculate(numbers)

print("Minimum:", result[0])
print("Maximum:", result[1])
print("Sum:", result[2])
print("Average:", result[3])
