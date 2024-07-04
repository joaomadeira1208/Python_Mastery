numbers = [1, 2, 3]
print(numbers)
print(*numbers)  # Unpacking Operator

values = list(range(5))
values = [*range(5)]
print(values)

first = [1, 2]
second = [3]
values = [*first, "a", *second, *"hello"]
print(values)

first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
print(combined)
