point = (1, 2)  # Is the same as 1, 2
print(type(point))

point = (1, 2) + (3, 4)  # This is a concatenation
print(point)

point = (1, 2) * 3  # This is a repetition
print(point)

point = tuple([1, 2])
print(point)

point = tuple("Hello World")
print(point)

point = (1, 2, 3)
print(point[0])
x, y, z = point
if 10 in point:
    print("Exists")

# point[0] = 10  # This will raise an error
