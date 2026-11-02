# Q6. Create Student with calculate_grade().
# Derive EngineeringStudent, MedicalStudent, and ManagementStudent.
# Override calculate_grade() according to different criteria.

class Student:
    def calculate_grade(self, marks):
        pass


class EngineeringStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 85:
            return "A"
        elif marks >= 70:
            return "B"
        else:
            return "C"


class MedicalStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 90:
            return "Distinction"
        elif marks >= 75:
            return "First Class"
        else:
            return "Pass"


class ManagementStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 80:
            return "Excellent"
        elif marks >= 60:
            return "Good"
        else:
            return "Pass"


students = [
    EngineeringStudent(),
    MedicalStudent(),
    ManagementStudent()
]

for student in students:
    print(student.calculate_grade(85))