n = int(input("Enter number of students: "))
marks = []
for i in range(n):
    marks.append(float(input("Enter marks: ")))

maximum = max(marks)
minimum = min(marks)
average = sum(marks) / n

count=0
for mark in marks:
    if mark > average:
        count += 1

print("Maximum:", maximum)
print("Minimum:", minimum)
print("Average:", average)
print("Above average:", count)