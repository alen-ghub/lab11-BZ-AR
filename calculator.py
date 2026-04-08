"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    try:
        return math.sqrt(a)

    except:
        if a < 0:
            raise ValueError

def hypotenuse(a, b):
    return math.hypot(a, b)

# First example
def add(a, b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return b / a

    except:
        if a == 0:
            raise ZeroDivisionError

def logarithm(a, b):
    try:
        return math.log(b, a)

    except:
        if a < 0:
            raise ValueError

def exponent(a, b):
    return a ** b


