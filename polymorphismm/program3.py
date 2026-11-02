# Q3. Create Vehicle with start().
# Derive Car, Bike, and Bus.
# Override start() to display different starting behavior.

class Vehicle:
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car starts with a key.")


class Bike(Vehicle):
    def start(self):
        print("Bike starts with a self-start button.")


class Bus(Vehicle):
    def start(self):
        print("Bus starts with a large engine.")


vehicles = [Car(), Bike(), Bus()]

for vehicle in vehicles:
    vehicle.start()