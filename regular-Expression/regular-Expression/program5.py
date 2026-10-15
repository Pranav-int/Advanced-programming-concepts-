import re

s = input("Enter text: ")
print(re.findall(r'[ \t\n]', s))