letters = ["a", "b", "c"]

for letter in letters:
    print(letter)
print("--------------------")
# Ugly way to get the index of the letter
for letter in enumerate(letters):
    print(letter)
    print(f"letter[0] = {letter[0]}, letter[1] = {letter[1]}")

print("--------------------")

# Better way to get the index of the letter
for index, letter in enumerate(letters):
    print(index, letter)
