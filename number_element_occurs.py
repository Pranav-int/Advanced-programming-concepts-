def count_occurrences(numbers, element):
    count = 0
    for num in numbers:
        if num == element:
            count += 1
    return count
numbers = [1, 2, 3, 2, 4, 2, 5]
element = 2
print("Number of occurrences:", count_occurrences(numbers, element))
