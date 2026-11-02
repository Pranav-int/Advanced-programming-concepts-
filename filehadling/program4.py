file = open("student.txt", "r")

for line in file:
    print(line, end="")

file.close()