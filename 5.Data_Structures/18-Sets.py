numbers = [1, 1, 2, 3, 4]
first = set(numbers)
print(first)
second = {1, 5}
print(second)

print(first | second)  # Union
print(first & second)  # Intersection
print(first - second)  # Difference
print(first ^ second)  # Symmetric difference

if 1 in first:
    print("Yes")


# To recap set is an unordered collection of unique items
# We cannot have duplicates in a set