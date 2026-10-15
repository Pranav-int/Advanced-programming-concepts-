import re

s = input("Enter paragraph: ")
print(re.findall(r'\b[1-9]\d{5}\b', s))