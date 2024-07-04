number = 100
while number > 0:
    print(number)
    number //= 2 # Integer division

print("-------------------------------")

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)
    