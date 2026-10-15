import re

s = input("Enter paragraph: ")
print(re.findall(r'\b\d{2}-\d{2}-\d{4}\b', s))