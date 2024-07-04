x = 10
y = 11

# This is the traditional way to swap variables
control = x
x = y
y = control

print(f"x: {x}, y: {y}")

x, y = y, x  # This is the Pythonic way to swap variables
a, b = 1, 2  # This is the Pythonic way to assign multiple variables

print(f"x: {x}, y: {y}")
