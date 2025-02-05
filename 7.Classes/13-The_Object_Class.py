class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

# Animal: Parent, Base
# Mammal: Child, Sub


class Mammal(Animal):
    def walk(self):
        print("walk")


m = Mammal()
print(isinstance(m, Mammal))
print(isinstance(m, Animal))
print(isinstance(m, object))  # Animal inherits from object

print("----------------")

print(issubclass(Mammal, Animal))
print(issubclass(Mammal, object))
