import pandas as pd

data = {
    "Amit": 45000,
    "Sneha": 60000,
    "Rahul": 75000,
    "Pooja": 50000,
    "Neha": 80000
}

s = pd.Series(data)

print("Series:")
print(s)

print("\nHighest salary:")
print(s.max())

print("\nLowest salary:")
print(s.min())

print("\nAverage salary:")
print(s.mean())

print("\nEmployees earning more than 50000:")
print(s[s > 50000])