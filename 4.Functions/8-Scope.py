message = "a"


def greet(name):
    global message
    message = "b"


# Message and name is a local variable
# print(message)  # NameError: name 'message' is not defined
# print(name)  # NameError: name 'name' is not defined

# Global variable
greet("Mosh")
print(message)  # a
