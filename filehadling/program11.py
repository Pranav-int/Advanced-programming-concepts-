file = open("student.txt", "r")

content = file.read()

words = content.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)

file.close()