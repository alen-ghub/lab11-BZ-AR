"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

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


