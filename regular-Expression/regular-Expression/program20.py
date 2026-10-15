import re

s = input("Enter filenames: ")
print(re.findall(r'\.([A-Za-z0-9]+)\b', s))