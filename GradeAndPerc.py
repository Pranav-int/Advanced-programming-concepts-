def calculate_result(marks):
    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return percentage, grade


# Example
marks = [85, 90, 78, 88, 92]
percentage, grade = calculate_result(marks)

print("Percentage:", percentage, "%")
print("Grade:", grade)
