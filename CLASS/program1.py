# Q1. Create a class Student with roll_no, name, and marks.
# Create objects for multiple students and display their details and percentage.

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def calculate_percentage(self):
        return sum(self.marks) / len(self.marks)

    def display(self):
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", self.calculate_percentage(), "%")
        print("------------------------")


# Creating objects
s1 = Student(1, "Pallavi", [80, 75, 90, 85, 88])
s2 = Student(2, "Rahul", [70, 65, 78, 80, 75])
s3 = Student(3, "Sneha", [90, 92, 88, 95, 91])

# Display student details
s1.display()
s2.display()
s3.display()