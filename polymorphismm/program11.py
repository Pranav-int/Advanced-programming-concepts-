# Q11. Create Product with name and price.
# Overload == and > operators to compare products based on price.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price


p1 = Product("Laptop", 60000)
p2 = Product("Mobile", 60000)

print("Prices Equal:", p1 == p2)
print("Laptop is More Expensive:", p1 > p2)