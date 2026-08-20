day1 = {101, 102, 103, 104}
day2 = {103, 104, 105, 106}

print("Unique visitors:", day1 | day2)
print("Returning visitors:", day1 & day2)
print("Only first day:", day1 - day2)
print("Only second day:", day2 - day1)