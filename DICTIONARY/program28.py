contacts = {
    "Amit": "9876543210",
    "Rahul": "9876501234"
}

contacts["Sneha"] = "9876512345"

name = input("Search contact: ")

if name in contacts:
    print("Phone:", contacts[name])
else:
    print("Contact not found")

name = input("Update contact name: ")

if name in contacts:
    contacts[name] = input("Enter new number: ")

name = input("Delete contact: ")

if name in contacts:
    del contacts[name]

print("All contacts:")

for name, number in contacts.items():
    print(name, number)