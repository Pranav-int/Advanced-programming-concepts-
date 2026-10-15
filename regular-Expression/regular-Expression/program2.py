import re

s = input("Enter sentence: ")
print(re.findall(r'\b[Aa]\w*', s))