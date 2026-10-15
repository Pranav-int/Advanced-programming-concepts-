import re

s = input("Enter research references: ")

doi = re.findall(r'\b10\.\d{4,9}/[^\s]+', s)
years = re.findall(r'\b(?:19|20)\d{2}\b', s)
emails = re.findall(r'[\w.+-]+@[\w-]+(?:\.[\w-]+)+', s)
urls = re.findall(r'https?://[^\s]+', s)

print("DOI:", doi)
print("Publication years:", years)
print("Emails:", emails)
print("URLs:", urls)