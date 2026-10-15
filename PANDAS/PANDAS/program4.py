import pandas as pd

data = {
    "Patient_ID": [1, 2, 3, 4, 5],
    "Patient_Name": ["Amit", "Sneha", "Rahul", "Pooja", "Neha"],
    "Age": [45, 65, 72, 30, 68],
    "Disease": ["Diabetes", "Heart", "BP", "Fever", "Diabetes"],
    "Medical_Charges": [30000, 60000, 75000, 20000, 55000]
}

df = pd.DataFrame(data)

print("Patients above 60:")
print(df[df["Age"] > 60])

print("\nAverage medical charge:")
print(df["Medical_Charges"].mean())

print("\nMaximum medical charge:")
print(df["Medical_Charges"].max())

print("\nPatients with charges greater than 50000:")
print(df[df["Medical_Charges"] > 50000])