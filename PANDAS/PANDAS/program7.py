import pandas as pd

data = {
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["Laptop", "Mobile", "TV", "Keyboard", "Monitor"],
    "Category": ["Electronics", "Electronics", "Electronics", "Accessories", "Electronics"],
    "Price": [50000, 20000, 30000, 1500, 12000],
    "Quantity": [2, 3, 1, 10, 2]
}

df = pd.DataFrame(data)

df["Total_Sales"] = df["Price"] * df["Quantity"]

print("DataFrame:")
print(df)

print("\nProducts with sales greater than 10000:")
print(df[df["Total_Sales"] > 10000])

print("\nProduct with maximum sales:")
print(df.loc[df["Total_Sales"].idxmax()])

print("\nAverage sales:")
print(df["Total_Sales"].mean())