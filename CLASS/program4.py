# Q4. Create a class Circle with radius.
# Define methods to calculate area and circumference.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius * self.radius

    def calculate_circumference(self):
        return 2 * math.pi * self.radius


# Creating object
c = Circle(7)

print("Radius:", c.radius)
print("Area:", c.calculate_area())
print("Circumference:", c.calculate_circumference())