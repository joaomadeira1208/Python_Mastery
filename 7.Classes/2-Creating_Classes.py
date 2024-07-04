class Point:
    def draw(self):
        print("draw")


point1 = Point()
print(type(point1))
print(isinstance(point1, Point))
point1.draw()
