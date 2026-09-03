
products = [
    ("Laptop", 50000, 2),
    ("Mouse", 500, 3),
    ("Keyboard", 1500, 2),
    ("Pen", 50, 10)
]

def total_value(product):
    return product[1] * product[2]


def expensive_products(products):
    return list(filter(lambda x: x[1] > 1000, products))


def sort_products(products):
    return sorted(products, key=lambda x: total_value(x))


print("Total value of each product:")
for product in products:
    print(product[0], ":", total_value(product))

print("\nProducts costing more than ₹1,000:")
print(expensive_products(products))

print("\nProducts sorted by total value:")
print(sort_products(products))
