import pandas as pd

data = {
    "Amit": 80,
    "Sneha": 72,
    "Rahul": 90,
    "Pooja": 65,
    "Neha": 85
}

s = pd.Series(data)

print("Series:")
print(s)

print("\nMarks of Rahul:")
print(s["Rahul"])

print("\nMaximum marks:")
print(s.max())

print("\nMinimum marks:")
print(s.min())

print("\nAverage marks:")
print(s.mean())

print("\nStudents scoring more than 75:")
print(s[s > 75])