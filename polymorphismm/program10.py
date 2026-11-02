# Q10. Create Student with name and total marks.
# Overload > and < operators to compare two students.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks

    def __lt__(self, other):
        return self.marks < other.marks


s1 = Student("Pallavi", 450)
s2 = Student("Rahul", 400)

print("Pallavi > Rahul:", s1 > s2)
print("Pallavi < Rahul:", s1 < s2)