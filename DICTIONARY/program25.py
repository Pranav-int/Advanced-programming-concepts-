students = {
    "Amit": 75,
    "Rahul": 85,
    "Sneha": 90
}

while True:
    print("\n1. Add")
    print("2. Update")
    print("3. Delete")
    print("4. Search")
    print("5. Display")
    print("6. Highest Marks")
    print("7. Average")
    print("8. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks

    elif choice == 2:
        name = input("Enter name: ")
        if name in students:
            students[name] = int(input("Enter new marks: "))
        else:
            print("Student not found")

    elif choice == 3:
        name = input("Enter name: ")
        if name in students:
            del students[name]
        else:
            print("Student not found")

    elif choice == 4:
        name = input("Enter name: ")
        if name in students:
            print(name, ":", students[name])
        else:
            print("Student not found")

    elif choice == 5:
        print(students)

    elif choice == 6:
        name = max(students, key=students.get)
        print("Highest:", name, students[name])

    elif choice == 7:
        print("Average:", sum(students.values()) / len(students))

    elif choice == 8:
        break

    else:
        print("Invalid choice")