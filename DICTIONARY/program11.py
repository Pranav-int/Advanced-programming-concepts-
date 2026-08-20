students = {
    "Amit": 75,
    "Rahul": 90,
    "Sneha": 85,
    "Priya": 95
}

name = max(students, key=students.get)

print("Highest marks:", name, students[name])