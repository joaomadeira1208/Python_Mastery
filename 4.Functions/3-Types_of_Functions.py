# 1-Performing a task
# 2-Return a value

# 1-Performing a task
def greet(name):
    print(f"Hi {name}")


# 2-Return a value
def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Mosh")
print(message)

print("-------------------------------")

print(greet("Mosh"))
