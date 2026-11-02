# Q6. Create a class ElectricityBill containing consumer number,
# consumer name, and units consumed.
# Calculate electricity bill according to different unit slabs.

class ElectricityBill:
    def __init__(self, consumer_no, consumer_name, units):
        self.consumer_no = consumer_no
        self.consumer_name = consumer_name
        self.units = units

    def calculate_bill(self):
        units = self.units

        if units <= 100:
            bill = units * 2

        elif units <= 200:
            bill = (100 * 2) + ((units - 100) * 3)

        elif units <= 300:
            bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)

        else:
            bill = (100 * 2) + (100 * 3) + (100 * 5) + ((units - 300) * 7)

        return bill

    def display(self):
        print("Consumer Number:", self.consumer_no)
        print("Consumer Name:", self.consumer_name)
        print("Units Consumed:", self.units)
        print("Electricity Bill: ₹", self.calculate_bill())


# Creating object
bill = ElectricityBill(1001, "Pallavi", 250)

bill.display()