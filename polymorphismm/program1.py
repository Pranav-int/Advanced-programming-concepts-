# Q1. Create Shape with area().
# Derive Circle, Rectangle, and Triangle.
# Override area() in each class and demonstrate runtime polymorphism.

import math

class Shape:
    def area(self):
        pass


class Circle(Shape):
    def area(self):
        return math.pi * 5 * 5


class Rectangle(Shape):
    def area(self):
        return 10 * 5


class Triangle(Shape):
    def area(self):
        return 0.5 * 10 * 8


shapes = [Circle(), Rectangle(), Triangle()]

for shape in shapes:
    print("Area:", shape.area())