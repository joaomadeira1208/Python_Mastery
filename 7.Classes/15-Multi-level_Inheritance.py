class Animal:
    def eat(self):
        print("eat")


class Bird(Animal):
    def fly(self):
        print("fly")


class Chicken(Bird):
    pass


# Chicken cannot fly
# If you want to use Inheritance, limit it to one or two levels.
