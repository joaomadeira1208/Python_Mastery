letters = ["a", "b", "c"]

# Add

# Add to the end of the list
letters.append("d")
letters.append("e")
letters.append("f")
print(letters)

# Add to a specific index
letters.insert(0, "-")
print(letters)

# Remove
letters.pop()
print(letters)

# Remove a specific index
letters.pop(0)
print(letters)

# Remove a specific item
letters.remove("b")
print(letters)

# Remove a range of items
del letters[0:2]
print(letters)

# Clear the list
letters.clear()
print(letters)
