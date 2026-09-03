students = [
    ("Rahul", 80),
    ("Priya", 90),
    ("Amit", 65),
    ("Sneha", 78),
    ("Ravi", 70)
]

def average_marks(students):
    marks = list(map(lambda x: x[1], students))
    return sum(marks) / len(marks)

def above_75(students):
    return list(filter(lambda x: x[1] > 75, students))

def sort_students(students):
    return sorted(students, key=lambda x: x[1])


print("Average Marks:", average_marks(students))
print("Above 75:", above_75(students))
print("Sorted Students:", sort_students(students))
