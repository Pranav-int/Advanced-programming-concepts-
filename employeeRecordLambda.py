employees = [
    ("Rahul", "IT", 60000),
    ("Priya", "HR", 45000),
    ("Amit", "Sales", 55000),
    ("Sneha", "IT", 70000)
]

high_salary = list(filter(lambda x: x[2] > 50000, employees))

increased_salary = list(
    map(lambda x: (x[0], x[1], x[2] * 1.10), employees)
)


sorted_employees = sorted(employees, key=lambda x: x[2])


print("Employees earning more than ₹50,000:")
print(high_salary)

print("\nSalaries after 10% increase:")
print(increased_salary)

print("\nEmployees sorted by salary:")
print(sorted_employees)
