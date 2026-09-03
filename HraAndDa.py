def calculate_gross_salary(basic_salary):
    hra = basic_salary * 0.20   # 20% HRA
    da = basic_salary * 0.10    # 10% DA

    gross_salary = basic_salary + hra + da

    return gross_salary


# Example
basic_salary = 30000
print("Gross Salary: ₹", calculate_gross_salary(basic_salary))
