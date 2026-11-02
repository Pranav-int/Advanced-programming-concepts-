file = open("students.txt", "r")

records = file.readlines()

file.close()

students = []

for line in records[1:]:
    roll, name, marks = line.strip().split(",")

    student = {
        "roll": roll,
        "name": name,
        "marks": float(marks)
    }

    students.append(student)


# Display all records
print("All Students:")

for student in students:
    print(student)


# Highest marks
highest = students[0]

for student in students:
    if student["marks"] > highest["marks"]:
        highest = student

print("\nHighest Marks:")
print(highest)


# Average marks
total = 0

for student in students:
    total += student["marks"]

average = total / len(students)

print("\nAverage Marks:", average)


# Students scoring more than 80
print("\nStudents scoring more than 80:")

for student in students:
    if student["marks"] > 80:
        print(student["name"])