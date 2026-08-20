data = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20
}

new_dict = {}

for key, value in data.items():
    if value not in new_dict.values():
        new_dict[key] = value

print(new_dict)