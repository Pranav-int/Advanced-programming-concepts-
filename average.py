def average(numbers):
    total = 0
    for i in numbers:
        total += i
    avg = total / len(numbers)
    return avg


numbers = [1, 2, 3, 4, 5]
print("Average of numbers:", average(numbers))
