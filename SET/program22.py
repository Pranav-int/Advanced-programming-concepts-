employee1 = {"Python", "Java", "SQL", "HTML"}
employee2 = {"Java", "Python", "CSS", "JavaScript"}

print("Common skills:", employee1 & employee2)
print("Unique to Employee 1:", employee1 - employee2)
print("Unique to Employee 2:", employee2 - employee1)
print("All skills:", employee1 | employee2)