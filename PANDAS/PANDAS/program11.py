import pandas as pd

data = {
    "P101": 45,
    "P102": 65,
    "P103": 72,
    "P104": 30,
    "P105": 68
}

s = pd.Series(data)

print("Average age:")
print(s.mean())

print("\nOldest patient:")
print(s.idxmax(), s.max())

print("\nYoungest patient:")
print(s.idxmin(), s.min())

print("\nPatients above 60:")
print(s[s > 60])