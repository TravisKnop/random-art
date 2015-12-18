import random
import math

# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.


def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""
    return random.choice([
#        new_func1(),
#        new_func2(),
        new_func3(),
#        new_func4(),
#        new_func5(),
#        new_func6()
        ])


def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr(x, y)

def new_func1():
    a = random.randint(1,5)
    b = random.randint(0,10)
    return lambda x, y: (math.tan(a * (x-a) ** b) + math.sin((y-b) ** a))**2

def new_func2():
    a = random.random()
    return lambda x, y: a*math.sin(x/a) * math.tan((x-y**(random.randint(1,10))/a)/a + random.randint(-2,2))

def new_func3():
    a = random.randint(1,6)
    b = random.randint(1,8)
    return lambda x, y: math.tan(a*(x)**2+a*y**2) * math.sin(b*x**a+y**b) + random.randint(-2,2)

def new_func4():
    return lambda x, y: math.tan(3*x+1)

def new_func5():
    return lambda x, y: math.tan(3*x+2)

def new_func6():
    return lambda x, y: math.tan(3*x)

create_expression()
