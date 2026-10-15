import re

s = input("Enter string: ")
print(re.sub(r' +', ' ', s))