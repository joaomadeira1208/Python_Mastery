class Point:

    # INSTANCE METHOD
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # CLASS METHOD
    @classmethod
    def zero(cls):
        return cls(0, 0)

    # INSTANCE METHOD
    def draw(self):
        print(f"Point: {self.x}, {self.y}")


point = Point.zero()
point.draw()
