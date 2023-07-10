"""
Default values for parameteres
When defining an function, parameters can
have default values. If the value is not
sent to the parameter, the default value will be
used.
Refactor: edit your code.
"""

# def sum(x, z=None, y):  # SyntaxError. z= None, y= ...
def sum(x, y, z=0):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

sum(5, 5)
sum(10, 15)
sum(15, 15)
sum(150, 150, 0)


