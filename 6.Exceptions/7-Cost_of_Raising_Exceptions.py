# Exceptions come with a cost. They are expensive in terms of performance.

from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age


xfactor = calculate_xfactor(-1)
"""
print("First code=", timeit(code1, number=10000))
print("Second code=", timeit(code2, number=10000))


# Think twice before using exceptions. They are expensive in terms of performance.
