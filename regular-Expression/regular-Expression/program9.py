import re

s = input("Enter string: ")
print(re.sub(r'[^a-zA-Z0-9 ]', '', s))