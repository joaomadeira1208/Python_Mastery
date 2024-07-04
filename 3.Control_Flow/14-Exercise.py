# My solution to the exercise

control = 0
for number in range(1, 10):
    if number % 2 == 0:
        print(number)
        control += 1

    if control == 4:
        print("4 even numbers found")
        break    

# Solution from the course

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
    if count == 4:
        print("4 even numbers found")
        break