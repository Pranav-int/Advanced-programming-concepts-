import re

s = input("Enter sentence: ")
words = re.findall(r'\b\w+\b', s)
print("Word count:", len(words))