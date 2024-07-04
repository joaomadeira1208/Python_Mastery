from array import array

numbers = array('i', [1, 2, 3, 4, 5])  # Unlike lists, arrays are typed
numbers.append(6)
numbers.insert(0, 0)
numbers.pop()
numbers.remove(1)

# Use array only when you need to store a large amount of numbers
# In other cases, use lists and tuples
