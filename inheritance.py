# 1. Create a class Employee with attributes emp_id, name, and salary. Create a derived class Manager that inherits from Employee and contains an additional attribute department. Display all employee and manager details and calculate the manager's annual salary.
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display_employee(self):
        print(self.emp_id, self.name, self.salary)

class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def display_manager(self):
        self.display_employee()
        print(self.department)

    def calculate_annual_salary(self):
        return self.salary * 12


# 2. Create a base class Vehicle with attributes brand and model. Create a derived class Car with additional attributes fuel_type and price. Define methods to display vehicle details and calculate the discounted price of the car.
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_vehicle(self):
        print(self.brand, self.model)

class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.price = price

    def display_car(self):
        self.display_vehicle()
        print(self.fuel_type, self.price)

    def calculate_discounted_price(self, discount_percent):
        return self.price - (self.price * (discount_percent / 100))


# 3. Create two classes Academic and Sports. The Academic class should store marks obtained by a student, while the Sports class should store sports points. Create a class Student that inherits from both classes and calculates the student's overall performance.
class Academic:
    def __init__(self, marks):
        self.marks = marks

class Sports:
    def __init__(self, sports_points):
        self.sports_points = sports_points

class Student(Academic, Sports):
    def __init__(self, marks, sports_points):
        Academic.__init__(self, marks)
        Sports.__init__(self, sports_points)

    def overall_performance(self):
        return self.marks + self.sports_points


# 4. Create classes PersonalDetails and ProfessionalDetails. Store personal information such as name and age in the first class and employee ID, designation, and salary in the second class. Create an Employee class that inherits from both classes and displays complete employee information.
class PersonalDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class ProfessionalDetails:
    def __init__(self, emp_id, designation, salary):
        self.emp_id = emp_id
        self.designation = designation
        self.salary = salary

class Employee(PersonalDetails, ProfessionalDetails):
    def __init__(self, name, age, emp_id, designation, salary):
        PersonalDetails.__init__(self, name, age)
        ProfessionalDetails.__init__(self, emp_id, designation, salary)

    def display_complete_information(self):
        print(self.name, self.age, self.emp_id, self.designation, self.salary)


# 5. Create a class Person containing name and age. Derive a class Student from Person with roll number and course. Further derive a class ResearchStudent from Student with research topic and guide name. Display all details.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll_number, course):
        super().__init__(name, age)
        self.roll_number = roll_number
        self.course = course

class ResearchStudent(Student):
    def __init__(self, name, age, roll_number, course, research_topic, guide_name):
        super().__init__(name, age, roll_number, course)
        self.research_topic = research_topic
        self.guide_name = guide_name

    def display_details(self):
        print(self.name, self.age, self.roll_number, self.course, self.research_topic, self.guide_name)


# 6. Create a base class BankAccount with account number and balance. Derive SavingsAccount from it with an interest rate. Further derive PremiumSavingsAccount with additional benefits. Define methods to calculate interest and display account details.
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * (self.interest_rate / 100)

class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_number, balance, interest_rate, bonus_points):
        super().__init__(account_number, balance, interest_rate)
        self.bonus_points = bonus_points

    def display_account_details(self):
        print(self.account_number, self.balance, self.interest_rate, self.bonus_points)


# 7. Create a base class Shape containing a method to display the name of the shape. Create three derived classes Circle, Rectangle, and Triangle. Each class should implement its own method to calculate the area.
import math

class Shape:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(self.name)

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


# 8. Create a base class Employee containing employee ID, name, and basic salary. Create derived classes Manager, Developer, and Tester. Each derived class should calculate salary differently based on its respective allowances.
class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

class Manager(Employee):
    def calculate_salary(self):
        return self.basic_salary + (self.basic_salary * 0.5)

class Developer(Employee):
    def calculate_salary(self):
        return self.basic_salary + (self.basic_salary * 0.3)

class Tester(Employee):
    def calculate_salary(self):
        return self.basic_salary + (self.basic_salary * 0.15)


# 9. Create a class Person. Derive Student and Faculty from Person. Create another class TeachingAssistant that inherits from both Student and Faculty. Display the details and demonstrate the use of multiple and hierarchical inheritance together.
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, student_id):
        Person.__init__(self, name)
        self.student_id = student_id

class Faculty(Person):
    def __init__(self, name, employee_id):
        Person.__init__(self, name)
        self.employee_id = employee_id

class TeachingAssistant(Student, Faculty):
    def __init__(self, name, student_id, employee_id):
        Student.__init__(self, name, student_id)
        Faculty.__init__(self, name, employee_id)

    def display_details(self):
        print(self.name, self.student_id, self.employee_id)


# 10. Create a base class Vehicle. Derive Car and Bike from Vehicle. Create a class SportsCar that inherits from Car and another classElectricBike that inherits from Bike. Add suitable attributes and methods to demonstrate a combination of inheritance types.
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors

class Bike(Vehicle):
    def __init__(self, brand, has_gears):
        super().__init__(brand)
        self.has_gears = has_gears

class SportsCar(Car):
    def __init__(self, brand, doors, top_speed):
        super().__init__(brand, doors)
        self.top_speed = top_speed

    def display_sportscar(self):
        print(self.brand, self.doors, self.top_speed)

class ElectricBike(Bike):
    def __init__(self, brand, has_gears, battery_range):
        super().__init__(brand, has_gears)
        self.battery_range = battery_range

    def display_electricbike(self):
        print(self.brand, self.has_gears, self.battery_range)


# 11. Create a base class Student with attributes roll_no, name, and course. Derive a class Result that stores marks in three subjects and calculates total marks, percentage, and grade.
class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course

class Result(Student):
    def __init__(self, roll_no, name, course, m1, m2, m3):
        super().__init__(roll_no, name, course)
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def generate_result(self):
        total = self.m1 + self.m2 + self.m3
        percentage = (total / 300) * 100
        if percentage >= 90:
            grade = "A"
        elif percentage >= 75:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        else:
            grade = "F"
        return total, percentage, grade


# 12. Create a class Product with product ID, name, and price. Derive ElectronicProduct with additional attributes such as brand and warranty. Calculate the final price after applying a discount.
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, brand, warranty):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.warranty = warranty

    def calculate_final_price(self, discount):
        return self.price - (self.price * (discount / 100))


# 13. Create classes Printer and Scanner with suitable methods for printing and scanning documents. Create a MultifunctionDevice class that inherits from both and supports both operations.
class Printer:
    def print_document(self, document):
        print(document)

class Scanner:
    def scan_document(self):
        return "Scanned Content"

class MultifunctionDevice(Printer, Scanner):
    def copy_document(self):
        content = self.scan_document()
        self.print_document(content)


# 14. Create classes Camera and Phone. The Camera class should provide methods for taking photographs, while Phone should provide methods for making calls. Create a Smartphone class inheriting from both.
class Camera:
    def take_photograph(self):
        print("Photograph taken")

class Phone:
    def make_call(self, number):
        print(number)

class Smartphone(Camera, Phone):
    def execute_smartphone_functions(self):
        self.take_photograph()
        self.make_call("9876543210")


# 15. Create a class Person with name and age. Derive Student with roll number and course. Further derive ResearchStudent with research topic and guide name.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll_number, course):
        super().__init__(name, age)
        self.roll_number = roll_number
        self.course = course

class ResearchStudent(Student):
    def __init__(self, name, age, roll_number, course, research_topic, guide_name):
        super().__init__(name, age, roll_number, course)
        self.research_topic = research_topic
        self.guide_name = guide_name


# 16. Create a class Person with name and age. Derive Student with roll number and course. Further derive ResearchStudent with research topic and guide name.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll_number, course):
        super().__init__(name, age)
        self.roll_number = roll_number
        self.course = course

class ResearchStudent(Student):
    def __init__(self, name, age, roll_number, course, research_topic, guide_name):
        super().__init__(name, age, roll_number, course)
        self.research_topic = research_topic
        self.guide_name = guide_name


# 17. Create a base class Animal with common attributes and methods. Derive Dog, Cat, and Cow classes and implement their specific sounds and behaviors.
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("Eating")

class Dog(Animal):
    def make_sound(self):
        print("Bark")
    
    def behavior(self):
        print("Guarding")

class Cat(Animal):
    def make_sound(self):
        print("Meow")
    
    def behavior(self):
        print("Chasing mice")

class Cow(Animal):
    def make_sound(self):
        print("Moo")
    
    def behavior(self):
        print("Grazing")


# 18. Create a class Person and derive Doctor and Patient. Create additional classes representing Surgeon and MedicalResearcher. Design the hierarchy so that the program demonstrates multiple inheritance along with hierarchical inheritance.
class Person:
    def __init__(self, name):
        self.name = name

class Doctor(Person):
    def __init__(self, name, license_number):
        Person.__init__(self, name)
        self.license_number = license_number

class Patient(Person):
    def __init__(self, name, symptom):
        Person.__init__(self, name)
        self.symptom = symptom

class Researcher:
    def __init__(self, lab_id):
        self.lab_id = lab_id

class Surgeon(Doctor):
    def __init__(self, name, license_number, surgery_type):
        super().__init__(name, license_number)
        self.surgery_type = surgery_type

class MedicalResearcher(Doctor, Researcher):
    def __init__(self, name, license_number, lab_id):
        Doctor.__init__(self, name, license_number)
        Researcher.__init__(self, lab_id)