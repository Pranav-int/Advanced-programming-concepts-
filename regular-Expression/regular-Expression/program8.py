import re

s = input("Enter sentence: ")
print(re.findall(r'\b\w*s\b', s, re.IGNORECASE))