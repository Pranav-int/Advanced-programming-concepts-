# Q12. Create a class FoodOrder with order ID, customer name,
# food item, quantity, and price.
# Use a constructor to initialize the order.
# Calculate total bill including tax.
# Implement a destructor to display an order completion message.

class FoodOrder:
    def __init__(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price

    def calculate_total(self):
        subtotal = self.quantity * self.price
        tax = subtotal * 0.05
        total = subtotal + tax

        return subtotal, tax, total

    def display_order(self):
        subtotal, tax, total = self.calculate_total()

        print("Order ID:", self.order_id)
        print("Customer Name:", self.customer_name)
        print("Food Item:", self.food_item)
        print("Quantity:", self.quantity)
        print("Price per Item: ₹", self.price)
        print("Subtotal: ₹", subtotal)
        print("Tax (5%): ₹", tax)
        print("Total Bill: ₹", total)

    def __del__(self):
        print("Order completed successfully.")


# Creating object
order = FoodOrder(101, "Pallavi", "Pizza", 2, 300)

# Display order
order.display_order()

# Destructor
del order