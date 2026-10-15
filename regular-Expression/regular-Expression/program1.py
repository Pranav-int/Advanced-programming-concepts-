import re

s = input("Enter string: ")
print(re.findall(r'\d', s))