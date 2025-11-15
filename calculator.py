"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# https://github.com/egladron/lab10-EL-JL
# Partner 1: Edwin Ladron de Guevara
# Partner 2: Joshua Lovett

import math

def square_root(a):
    if a < 0 :
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):
    math.hypot(a, b)

def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def logarithm(a, b):
    try:
        return math.log(b, a)
    except ValueError:
        raise ValueError

def exponent(a, b):
    return a ** b