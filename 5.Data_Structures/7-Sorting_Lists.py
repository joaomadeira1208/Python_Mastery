numbers = [3, 51, 2, 8, 6]
numbers.sort()
print("First test")
print(numbers)
numbers.sort(reverse=True)
print("Second test")
print(numbers)

# The sorted() function returns a new list and does not modify the original list
numbers = [3, 51, 2, 8, 6]
print("Third test")
print(sorted(numbers))
print(numbers)

print(sorted(numbers, reverse=True))


# Sorting a list of tuples
items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print("Sorting list of tuples")
print(items)
