# items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]


# def sort_item(item):
#     return item[1]


# items.sort(key=sort_item)
# print("Sorting list of tuples")
# print(items)

# Improve the code above using lambda functions

items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]
items.sort(key=lambda item: item[1])
print("Sorting list of tuples")
print(items)
