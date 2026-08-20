numbers = [2, 7, 11, 15]
target = 9

data = {}

for num in numbers:
    required = target - num

    if required in data:
        print(required, num)
        break

    data[num] = True