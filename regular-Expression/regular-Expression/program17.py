import re

s = input("Enter sentence: ")

pattern = r'\b(\w+)\s+\1\b'
print(re.findall(pattern, s, re.IGNORECASE))