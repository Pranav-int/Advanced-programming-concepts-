import pandas as pd

data = {
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["Laptop", "Mobile", "Keyboard", "Mouse", "Monitor"],
    "Category": ["Electronics", "Electronics", "Accessories", "Accessories", "Electronics"],
    "Price": [50000, 30000, 2000, 1000, 15000],
    "Quantity": [2, 5, 10, 20, 4]
}

df = pd.DataFrame(data)

df["Total_Amount"] = df["Price"] * df["Quantity"]

print(df)

print("\nProduct with highest total sales:")
print(df.loc[df["Total_Amount"].idxmax()])