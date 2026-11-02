# Q11. Create a class ShoppingCart with customer name and cart ID.
# Initialize values using a constructor.
# Implement methods to add products, remove products,
# and calculate the total bill.
# Use a destructor to display a message when the cart is destroyed.

class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = []

    def add_product(self, name, price):
        self.products.append([name, price])
        print(name, "added to cart.")

    def remove_product(self, name):
        for product in self.products:
            if product[0] == name:
                self.products.remove(product)
                print(name, "removed from cart.")
                return

        print("Product not found.")

    def calculate_total(self):
        total = 0

        for product in self.products:
            total += product[1]

        return total

    def display_cart(self):
        print("\nCustomer Name:", self.customer_name)
        print("Cart ID:", self.cart_id)
        print("Products:")

        for product in self.products:
            print(product[0], "₹", product[1])

        print("Total Bill: ₹", self.calculate_total())

    def __del__(self):
        print("Shopping Cart object destroyed.")


# Creating object
cart = ShoppingCart("Pallavi", "C101")

# Adding products
cart.add_product("Laptop", 50000)
cart.add_product("Mouse", 1000)
cart.add_product("Keyboard", 2000)

# Display cart
cart.display_cart()

# Remove product
cart.remove_product("Mouse")

# Display updated cart
cart.display_cart()

# Destructor will execute when object is destroyed
del cart