word = input("Enter word to search: ")

file = open("student.txt", "r")

count = 0
line_number = 0
lines_found = []

for line in file:
    line_number += 1

    words = line.split()

    for w in words:
        if w == word:
            count += 1
            if line_number not in lines_found:
                lines_found.append(line_number)

print("Occurrences:", count)
print("Line numbers:", lines_found)

file.close()