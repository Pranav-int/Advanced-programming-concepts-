import re

s = input("Enter text: ")

s = re.sub(r'<[^>]*>', '', s)
s = re.sub(r'[^\w\s]', '', s)
s = re.sub(r'\s+', ' ', s)

print(s.strip())