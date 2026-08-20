python_students = {"Amit", "Rahul", "Priya", "Sneha"}
java_students = {"Priya", "Sneha", "Rohan", "Neha"}

both = python_students & java_students
only_one = python_students ^ java_students

print("Students in both courses:", both)
print("Students in only one course:", only_one)