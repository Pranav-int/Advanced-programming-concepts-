# Q3. Create a class Rectangle with length and breadth.
# Define methods to calculate area and perimeter.

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth

    def calculate_perimeter(self):
        return 2 * (self.length + self.breadth)


# Creating object
r = Rectangle(10, 5)

print("Length:", r.length)
print("Breadth:", r.breadth)
print("Area:", r.calculate_area())
print("Perimeter:", r.calculate_perimeter())