import pandas as pd

df = pd.read_csv("students.csv")

print("First 5 records:")
print(df.head())

print("\nLast 5 records:")
print(df.tail())

df["Total"] = df["Python"] + df["DBMS"] + df["Maths"]

df["Average"] = df["Total"] / 3

print("\nTotal and Average marks:")
print(df)

print("\nStudents with average greater than 75:")
print(df[df["Average"] > 75])

print("\nStudent with highest average:")
print(df.loc[df["Average"].idxmax()])

print("\nAverage marks of each subject:")
print(df[["Python", "DBMS", "Maths"]].mean())