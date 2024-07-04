import random
import string

print(random.random())
print(random.randint(1, 10))  # 1 and 10 included
print(random.choice([1, 2, 3, 4]))  # Pick one random number of the array
print(random.choices([1, 2, 3, 4], k=2))  # Pick k random numbers of the array
print(random.choices("abcdefghhi", k=4))

# Random Password
print("".join(random.choices(string.ascii_letters+string.digits, k=4)))

# Shuffling array
numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)
