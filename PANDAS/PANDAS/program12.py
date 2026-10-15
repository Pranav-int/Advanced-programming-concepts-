import pandas as pd

data = {
    "Amit": 80,
    "Sneha": 70,
    "Rahul": 95,
    "Pooja": 65,
    "Neha": 92
}

s = pd.Series(data)

print("Average attendance:")
print(s.mean())

print("\nStudents below 75%:")
print(s[s < 75])

print("\nStudents above 90%:")
print(s[s > 90])

print("\nHighest attendance:")
print(s.max())