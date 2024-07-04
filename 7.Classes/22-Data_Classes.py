# INSTEAD OF WRITING THIS CODE
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

# WE CAN WRITE THIS CODE
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(p1 == p2)

# If you are using classes with no methods and only attributes, you might want to use namedtuples
# It is a class that comes with Python's standard library
# These namedtuples are IMMUTABLE
