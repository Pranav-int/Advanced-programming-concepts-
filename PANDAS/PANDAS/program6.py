import pandas as pd

data = {
    "Student_ID": [1, 2, 3, 4, 5],
    "Name": ["Amit", "Sneha", "Rahul", "Pooja", "Neha"],
    "Department": ["CSE", "IT", "CSE", "IT", "CSE"],
    "Total_Classes": [100, 100, 120, 100, 110],
    "Classes_Attended": [80, 70, 90, 60, 100]
}

df = pd.DataFrame(data)

df["Attendance_Percentage"] = (
    df["Classes_Attended"] / df["Total_Classes"]
) * 100

print(df)

print("\nStudents with attendance below 75%:")
print(df[df["Attendance_Percentage"] < 75])