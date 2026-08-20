students = {
    "Amit": 75,
    "Rahul": 90,
    "Sneha": 65,
    "Priya": 95
}

name = min(students, key=students.get)

print("Lowest marks:", name, students[name])