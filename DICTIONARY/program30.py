students = {
    "Amit": "Computer",
    "Rahul": "IT",
    "Sneha": "Computer",
    "Priya": "Mechanical",
    "Riya": "IT"
}

groups = {}

for name, department in students.items():
    if department not in groups:
        groups[department] = []
    groups[department].append(name)

print(groups)