from abc import ABC, abstractmethod


class TextBox():
    def draw(self):
        print("Drawing a textbox")


class DropDownList():
    def draw(self):
        print("Drawing a dropdownlist")


def draw(controls):
    for control in controls:
        # if it walks like a duck and quacks like a duck, it must be a duck. This means that the draw method must be present in the classes that are passed to the draw function.
        control.draw()


draw([TextBox(), DropDownList()])
