# Q6. Create abstract Transport with calculate_fare(distance).
# Implement Bus, Train, Taxi, and Flight.

from abc import ABC, abstractmethod


class Transport(ABC):

    @abstractmethod
    def calculate_fare(self, distance):
        pass


class Bus(Transport):
    def calculate_fare(self, distance):
        return distance * 2


class Train(Transport):
    def calculate_fare(self, distance):
        return distance * 1.5


class Taxi(Transport):
    def calculate_fare(self, distance):
        return distance * 10


class Flight(Transport):
    def calculate_fare(self, distance):
        return distance * 8


distance = 100

transports = [Bus(), Train(), Taxi(), Flight()]

for transport in transports:
    print("Fare:", transport.calculate_fare(distance))