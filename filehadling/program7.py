file = open("student.txt", "r")

content = file.read()

print("Total characters:", len(content))

file.close()