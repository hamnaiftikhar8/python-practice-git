import math
from functools import *

def add_numbers(a = 2, b=9):
    result = a + b
    return result

def calculate_power(a, b):
    result = math.pow(a,b)
    return result

print(add_numbers(10,9))

print(add_numbers(b = 6))

print(calculate_power(3,2))


#partial functions

def f(a, b, c):
    return 100 * a + 5 + b - 10/c

result = partial(f, 2, 2)

print(result(2))