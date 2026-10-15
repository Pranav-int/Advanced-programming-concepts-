import re

s = input("Enter student details: ")

pattern = r'Name:\s*(\w+),\s*Roll:\s*(\d+),\s*Marks:\s*(\d+)'
result = re.findall(pattern, s)

for name, roll, marks in result:
    print("Name:", name)
    print("Roll Number:", roll)
    print("Marks:", marks)