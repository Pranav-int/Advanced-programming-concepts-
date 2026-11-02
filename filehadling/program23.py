file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")

lines1 = file1.readlines()
lines2 = file2.readlines()

file1.close()
file2.close()

same = True

limit = min(len(lines1), len(lines2))

for i in range(limit):
    if lines1[i] != lines2[i]:
        print("Files are different.")
        print("First difference at line:", i + 1)

        print("File 1:", lines1[i], end="")
        print("File 2:", lines2[i], end="")

        same = False
        break

if same:
    if len(lines1) == len(lines2):
        print("Files are identical.")
    else:
        print("Files are different.")
        print("First difference at line:", limit + 1)