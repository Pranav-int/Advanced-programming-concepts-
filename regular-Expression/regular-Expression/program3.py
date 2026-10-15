import re

s = input("Enter string: ")
vowels = re.findall(r'[aeiouAEIOU]', s)
print("Vowel count:", len(vowels))