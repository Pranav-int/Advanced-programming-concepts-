import re

s = input("Enter text: ")
print(re.findall(r'https?://[^\s]+', s))