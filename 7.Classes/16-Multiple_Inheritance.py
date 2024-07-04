# Like multi-level inheritance, multiple inheritance is a source of complexity and ambiguity.

class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")


# The order of inheritance matters, if they have methods in common.
class Manager(Employee, Person):  # Multiple Inheritance
    pass


manager = Manager()
manager.greet()


# Good Example of Multiple Inheritance


class Flyer:
    def fly(self):
        print("Fly")


class Swimmer:
    def swim(self):
        print("Swim")


class FlyingFish(Flyer, Swimmer):
    pass
