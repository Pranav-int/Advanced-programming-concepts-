file = open("student.txt", "r")

lines = file.readlines()

for line in reversed(lines):
    print(line, end="")

file.close()