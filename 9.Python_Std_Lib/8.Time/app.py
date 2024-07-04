import time


def add_1000000(value):
    for i in range(1000000):
        value = value + 1


start = time.time()
add_1000000(0)
end = time.time()

duration = float(end - start)
print(duration)
