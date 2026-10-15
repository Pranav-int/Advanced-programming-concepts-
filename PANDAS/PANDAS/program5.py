import pandas as pd

data = {
    "Order_ID": [1, 2, 3, 4, 5],
    "Customer": ["Amit", "Sneha", "Rahul", "Pooja", "Neha"],
    "Product": ["Laptop", "Mobile", "Tablet", "Monitor", "Printer"],
    "Quantity": [2, 3, 2, 4, 1],
    "Price": [40000, 20000, 15000, 10000, 25000],
    "Discount": [2000, 1000, 500, 1000, 2000]
}

df = pd.DataFrame(data)

df["Final_Amount"] = (df["Quantity"] * df["Price"]) - df["Discount"]

print("All Orders:")
print(df)

print("\nOrders above 5000:")
print(df[df["Final_Amount"] > 5000])

print("\nHighest-value order:")
print(df.loc[df["Final_Amount"].idxmax()])

print("\nAverage order value:")
print(df["Final_Amount"].mean())