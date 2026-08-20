employees = {
    101: "Amit",
    102: "Rahul",
    103: "Sneha",
    104: "Priya"
}

id = int(input("Enter employee ID: "))

if id in employees:
    print("Employee exists")
else:
    print("Employee does not exist")