numbers = [1, 2, 3, 4]
print("LIST UNPACKING")
print("--------------------")

first, second, third, fourth = numbers
print(first)
print(second)
print(third)
print(fourth)
print("--------------------")

first, second, *others = numbers
print(first)
print(second)
print(others)
print("--------------------")

first, *others, last = numbers
print(first)
print(others)
print(last)
print("--------------------")
