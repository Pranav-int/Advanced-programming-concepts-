def calculate_total(marks):
    return sum(marks)


def calculate_percentage(total):
    return total / 5


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def class_average(students):
    total = 0
    for student in students:
        total += calculate_percentage(calculate_total(student["marks"]))
    return total / len(students)


def highest_scorer(students):
    return max(students, key=lambda x: calculate_total(x["marks"]))


def lowest_scorer(students):
    return min(students, key=lambda x: calculate_total(x["marks"]))



students = [
    {"name": "Rahul", "roll": 1, "marks": [80, 75, 90, 85, 88]},
    {"name": "Priya", "roll": 2, "marks": [90, 92, 85, 95, 90]},
    {"name": "Amit", "roll": 3, "marks": [65, 70, 60, 75, 68]}
]


for student in students:
    total = calculate_total(student["marks"])
    percentage = calculate_percentage(total)
    grade = calculate_grade(percentage)

    print("Name:", student["name"])
    print("Roll Number:", student["roll"])
    print("Total:", total)
    print("Percentage:", percentage, "%")
    print("Grade:", grade)
    print()


print("Class Average:", class_average(students), "%")


high = highest_scorer(students)
print("Highest Scorer:", high["name"])


low = lowest_scorer(students)
print("Lowest Scorer:", low["name"])
