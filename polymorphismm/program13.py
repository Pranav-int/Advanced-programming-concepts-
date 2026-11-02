# Q13. Create Person with display_role().
# Derive Student, Faculty, and Administrator.
# Store objects in a list and invoke the same method using a loop.

class Person:
    def display_role(self):
        pass


class Student(Person):
    def display_role(self):
        print("Role: Student")


class Faculty(Person):
    def display_role(self):
        print("Role: Faculty")


class Administrator(Person):
    def display_role(self):
        print("Role: Administrator")


people = [
    Student(),
    Faculty(),
    Administrator()
]

for person in people:
    person.display_role()