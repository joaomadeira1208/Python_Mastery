class Point:
    default_color = "red"  # Class level attribute

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"{self.x}, {self.y}")


Point.default_color = "yellow"

point = Point(1, 2)
print(point.default_color)
print(Point.default_color)
point.draw()

another = Point(3, 4)
another.draw()
print(another.default_color)

# The x and y attributes are instance attributes
# They are unique to each object
