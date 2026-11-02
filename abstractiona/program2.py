# Q2. Create abstract Vehicle with start() and stop().
# Derive Car, Bike, and Bus and implement these methods.

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car Started")

    def stop(self):
        print("Car Stopped")


class Bike(Vehicle):
    def start(self):
        print("Bike Started")

    def stop(self):
        print("Bike Stopped")


class Bus(Vehicle):
    def start(self):
        print("Bus Started")

    def stop(self):
        print("Bus Stopped")


vehicles = [Car(), Bike(), Bus()]

for vehicle in vehicles:
    vehicle.start()
    vehicle.stop()