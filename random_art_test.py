import random
import math

# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.


def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""
    expr = random.choice([anti_asterisk(), hoop(), top_right(), most_random()])
    return expr


def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr(x, y)

"""def blah_blah():
    func = lambda x, y: "[cos(x), sin()]
    return eval(func)

def blah_blah1():
    func = lambda x, y: x*y/random.randint(1,100) ** 0.5
    return func


def blah2():
    z = lambda x, y: math.sin(x)*math.sin(y)*1/random.triangular()
    return z"""

#def asterisk():
#    a = lambda x, y: math.fabs(1-x*y)**random.triangular()
#    return a

def anti_asterisk():
    return lambda x, y: (x-random.randint(1,3))**2 + (y+random.randint(0,5))**2

def top_right():
    return lambda x, y: random.lognormvariate(x*y, random.random())

def hoop():
    a = random.triangular()
    return lambda x, y: ((a*(math.fabs(x+float(random.randint(1,4)**2 - math.cos(y*random.randint(1,5))**a)*random.random()))))

def most_random():
    w = random.randint(1,4)
    if w == 1:
        return lambda x, y: (math.sin(x)*y) + (math.sin(y)*x)
    if w == 2:
        return lambda x, y: (math.sin(x)*y) - (math.sin(y)*x)
    if w == 3:
        return lambda x, y: (math.sin(x)*y) * (math.sin(y)*x)
