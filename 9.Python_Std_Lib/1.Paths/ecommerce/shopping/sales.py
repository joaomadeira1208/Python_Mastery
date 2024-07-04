
def calc_tax():
    print("calc_tax")


def calc_shipping():
    print("calc_shipping")


if __name__ == "__main__":
    print("Sales started")
    calc_tax()
    print("Sales finished")
else:
    print("Sales imported")
    print(__name__)
