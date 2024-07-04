class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):  # eq stands for equal
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):  # gt stands for greater than
        return self.x > other.x and self.y > other.y


point = Point(10, 20)
another = Point(1, 2)
print(point == another)  # False before adding __eq__ method
print(point > another)
