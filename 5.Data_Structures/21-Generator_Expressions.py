from sys import getsizeof

values = (x*2 for x in range(5))
print(values)  # This is a generator object
for x in values:
    print(x)

# Try to switch the range to 100000 and see the difference in memory usage
values = [x*2 for x in range(1000)]
print("List:", getsizeof(values))

values = (x*2 for x in range(1000))
print("Generator:", getsizeof(values))
