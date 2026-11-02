# Q7. Create a class MobilePhone with brand, model, storage, and price.
# Define methods to display specifications and calculate price after discount.

class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display_specifications(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Storage:", self.storage)
        print("Price:", self.price)

    def price_after_discount(self, discount):
        discount_amount = self.price * discount / 100
        final_price = self.price - discount_amount
        return final_price


# Creating object
phone = MobilePhone("Samsung", "Galaxy A55", "256 GB", 40000)

phone.display_specifications()

discount = 10
print("Discount:", discount, "%")
print("Price After Discount:", phone.price_after_discount(discount))