import re

s = input("Enter Python source line: ")

comments = re.findall(r'#.*', s)
print("Comments:", comments)