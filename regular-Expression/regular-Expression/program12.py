import re

email = input("Enter email: ")

if re.fullmatch(r'[\w.+-]+@[\w-]+(\.[\w-]+)+', email):
    print("Valid email")
else:
    print("Invalid email")