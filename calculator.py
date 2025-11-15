"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# https://github.com/egladron/lab10-EL-JL
# Partner 1: Edwin Ladron de Guevara
# Partner 2: Joshua Lovett

import math

def add(a, b): 
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Unable to divide by zero")
    return a / b
def log(a,b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid input for logarithm")
    return math.log(b, a)
def exp(a, b):
    return a ** b
