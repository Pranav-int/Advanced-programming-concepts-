def read_employees():
    file = open("employees.txt", "r")

    employees = []

    for line in file:
        emp_id, name, department, salary = line.strip().split(",")

        employees.append({
            "id": emp_id,
            "name": name,
            "department": department,
            "salary": float(salary)
        })

    file.close()

    return employees


def display_employees():
    employees = read_employees()

    for emp in employees:
        print(emp)


def highest_paid():
    employees = read_employees()

    highest = employees[0]

    for emp in employees:
        if emp["salary"] > highest["salary"]:
            highest = emp

    print("Highest Paid Employee:")
    print(highest)


def average_salary():
    employees = read_employees()

    total = 0

    for emp in employees:
        total += emp["salary"]

    print("Average Salary:", total / len(employees))


def above_salary(amount):
    employees = read_employees()

    for emp in employees:
        if emp["salary"] > amount:
            print(emp)


display_employees()

highest_paid()

average_salary()

above_salary(50000)