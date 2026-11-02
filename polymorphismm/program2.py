# Q2. Create Employee with calculate_salary().
# Derive Manager, Developer, and Tester.
# Override calculate_salary() according to role.

class Employee:
    def calculate_salary(self):
        pass


class Manager(Employee):
    def calculate_salary(self):
        return 70000


class Developer(Employee):
    def calculate_salary(self):
        return 60000


class Tester(Employee):
    def calculate_salary(self):
        return 50000


employees = [Manager(), Developer(), Tester()]

for employee in employees:
    print("Salary:", employee.calculate_salary())