file = open("student.txt", "r")

content = file.read()

words = content.split()

print("Total words:", len(words))

file.close()