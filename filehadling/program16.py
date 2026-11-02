file = open("student.txt", "r")

content = file.read()

file.close()

output = open("uppercase.txt", "w")

output.write(content.upper())

output.close()

print("Uppercase file created.")