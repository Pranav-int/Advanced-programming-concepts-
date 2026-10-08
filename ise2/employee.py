
import csv

salary = float(input("Enter minimum salary: "))
experience = int(input("Enter minimum experience: "))
department = input("Enter department: ")

with open("employees.csv", "r") as file:
    data = csv.DictReader(file)

    for employee in data:
        if float(employee["salary"]) >= salary and int(employee["Experience"]) >= experience and employee["Department"].lower() == department.lower():
            print(employee["Name"], employee["Salary"], employee["Experience"], employee["Department"])


