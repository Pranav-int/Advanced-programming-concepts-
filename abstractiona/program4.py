
# Q4. Create abstract FoodOrder with calculate_bill()
# and delivery_charge().
# Derive RestaurantOrder and HomeDeliveryOrder.

from abc import ABC, abstractmethod


class FoodOrder(ABC):

    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def delivery_charge(self):
        pass


class RestaurantOrder(FoodOrder):
    def calculate_bill(self):
        return 500

    def delivery_charge(self):
        return 0


class HomeDeliveryOrder(FoodOrder):
    def calculate_bill(self):
        return 500

    def delivery_charge(self):
        return 50


orders = [RestaurantOrder(), HomeDeliveryOrder()]

for order in orders:
    total = order.calculate_bill() + order.delivery_charge()
    print("Total Bill:", total)