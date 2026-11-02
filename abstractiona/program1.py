# Q1. Create an abstract class Shape with abstract method area().
# Derive Circle, Rectangle, and Triangle and implement area().

from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
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


print("Circle Area:", Circle().area())
print("Rectangle Area:", Rectangle().area())
print("Triangle Area:", Triangle().area())