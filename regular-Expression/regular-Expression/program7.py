import re

s = input("Enter sentence: ")
print(re.findall(r'\b[A-Za-z]{5}\b', s))