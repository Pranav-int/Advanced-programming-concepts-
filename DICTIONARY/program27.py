
products = {
    "Pen": 20,
    "Book": 5,
    "Bag": 15
}

products["Pencil"] = 8
products["Pen"] = 25

del products["Bag"]

name = input("Search product: ")

if name in products:
    print("Quantity:", products[name])
else:
    print("Product not found")

print("Products below 10:")

for name, quantity in products.items():
    if quantity < 10:
        print(name, quantity)