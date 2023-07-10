"""
Named and unnamed arguments in Python functions
Named arguments has name with an equal sign
Unnamed arguments recieves only the argument (value)
"""

def sum(x, y, z):
    # Definition
    print(f'{x=} {y=} {z=}', '|', 'x + y + z=',x + y + z)

sum(5, 5, 3)
# sum(7, y= 7, 7)  # SyntaxError. y=7, z=7, ...
sum(7, 7, z=7)
sum(y=5, x=3, z= 3)