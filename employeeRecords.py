employees = [
    ("Rahul", 30000),
    ("Priya", 45000),
    ("Amit", 25000),
    ("Sneha", 50000)
]

employees.sort(key=lambda x: x[1])

print(employees)
