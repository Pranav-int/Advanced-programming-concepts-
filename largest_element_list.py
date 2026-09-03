def largest(numbers):
    largest_number = numbers[0]

    for num in numbers:
        if num > largest_number:
            largest_number = num

    return largest_number


numbers = [10, 25, 7, 42, 18]
print("Largest element:", largest(numbers))
