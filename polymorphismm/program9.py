# Q9. Create Distance with feet and inches.
# Overload + operator to add two distance objects.
# Display the result in normalized form.

class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        total_inches = self.inches + other.inches
        total_feet = self.feet + other.feet

        if total_inches >= 12:
            total_feet += total_inches // 12
            total_inches = total_inches % 12

        return Distance(total_feet, total_inches)

    def display(self):
        print(self.feet, "feet", self.inches, "inches")


d1 = Distance(5, 8)
d2 = Distance(4, 7)

d3 = d1 + d2

d3.display()