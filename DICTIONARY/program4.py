students = {
    "Amit": 70,
    "Rahul": 80,
    "Sneha": 90
}

name = input("Enter student name: ")
marks = int(input("Enter new marks: "))

if name in students:
    students[name] = marks
    print(students)
else:
    print("Student not found")