employee = {
    "id": 101,
    "name": "Rahul",
    "department": "IT",
    "salary": 50000
}

key = input("Enter key: ")

if key in employee:
    print("Value:", employee[key])
else:
    print("Key not found")