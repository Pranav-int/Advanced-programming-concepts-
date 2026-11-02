# Q10. Create a class Vehicle containing vehicle number, model,
# rental rate, and availability.
# Implement methods to rent and return a vehicle
# and calculate rental charges based on number of days.

class Vehicle:
    def __init__(self, vehicle_no, model, rental_rate):
        self.vehicle_no = vehicle_no
        self.model = model
        self.rental_rate = rental_rate
        self.availability = True

    def rent_vehicle(self):
        if self.availability:
            self.availability = False
            print("Vehicle rented successfully.")
        else:
            print("Vehicle is not available.")

    def return_vehicle(self, days):
        if not self.availability:
            self.availability = True
            charges = self.rental_rate * days
            print("Vehicle returned successfully.")
            print("Number of Days:", days)
            print("Rental Charges: ₹", charges)
        else:
            print("Vehicle was not rented.")

    def display(self):
        print("Vehicle Number:", self.vehicle_no)
        print("Model:", self.model)
        print("Rental Rate per Day: ₹", self.rental_rate)
        print("Available:", self.availability)


# Creating object
v = Vehicle("MH12AB1234", "Swift", 1500)

v.display()

# Rent vehicle
v.rent_vehicle()

# Return vehicle after 3 days
v.return_vehicle(3)

v.display()