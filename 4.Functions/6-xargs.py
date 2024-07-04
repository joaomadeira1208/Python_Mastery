def multiply(*numbers):
    print(numbers)


multiply(1, 2, 3, 4, 5)

print("-------------------------------")


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("Multiply: 1 * 2 * 3 * 4 * 5 = ")
print(multiply(1, 2, 3, 4, 5))
