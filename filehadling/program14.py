file = open("student.txt", "r")

content = file.read()

old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

content = content.replace(old_word, new_word)

file.close()

file = open("student.txt", "w")

file.write(content)

file.close()

print("Word replaced successfully.")