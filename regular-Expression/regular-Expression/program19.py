import re

number = input("Enter vehicle number: ")

pattern = r'[A-Z]{2}\d{2}[A-Z]{1,2}\d{4}'

if re.fullmatch(pattern, number):
    print("Valid vehicle number")
else:
    print("Invalid vehicle number")