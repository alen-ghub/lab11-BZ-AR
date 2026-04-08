#Example: https://github.com/alen-ghub/lab11-BZ-AR.git
# Partner 1: Brian Zheng
# Partner 2: Alen Rodriguez


import math

def square_root(a):
    try:
        return math.sqrt(a)

    except:
        if a < 0:
            raise ValueError

def hypotenuse(a, b):
    return math.hypot(a, b)
def add(a, b):
    return a + b


# First example
def add(a, b):
    return a + b

def subtract(a,b):
    return a - b


def logarithm(a, b):
    try:
        return math.log(b, a)

    except:
        if a < 0:
            raise ValueError



def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def exp(a, b):
    return a ** b