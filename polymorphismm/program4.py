# Q4. Create Animal with sound().
# Create Dog, Cat, Cow, and Lion.
# Override sound() in each class.

class Animal:
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Dog: Woof")


class Cat(Animal):
    def sound(self):
        print("Cat: Meow")


class Cow(Animal):
    def sound(self):
        print("Cow: Moo")


class Lion(Animal):
    def sound(self):
        print("Lion: Roar")


animals = [Dog(), Cat(), Cow(), Lion()]

for animal in animals:
    animal.sound()