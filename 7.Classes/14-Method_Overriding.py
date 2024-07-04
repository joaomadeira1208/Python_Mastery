# class Animal:
#     def __init__(self):
#         self.age = 1

#     def eat(self):
#         print("eat")

# # Animal: Parent, Base
# # Mammal: Child, Sub


# class Mammal(Animal):
#     def __init__(self):
#         self.weight = 2

#     def walk(self):
#         print("walk")


# # Will occur an error because the __init__ method in the Mammal class is overriding the __init__ method in the Animal class
# # m = Mammal()
# # print(m.age)
# # print(m.weight)

class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")

# Animal: Parent, Base
# Mammal: Child, Sub


class Mammal(Animal):
    def __init__(self):
        print("Mammal Constructor")
        self.weight = 2
        super().__init__()

    def walk(self):
        print("walk")


m = Mammal()
print(m.age)
print(m.weight)
