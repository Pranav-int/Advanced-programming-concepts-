dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"x": 20, "y": 30, "z": 40}

common = []

for value in dict1.values():
    if value in dict2.values():
        common.append(value)

print("Common values:", common)