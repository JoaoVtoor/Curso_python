"""
Introduction to functions (def) in Python
Functions are code snippets used for
replicate determined action along the code.
They can recieve values for parameters (arguments)
and return an specific value.
By default, functions in python returns None.
"""

def print_out(a, b, c):  # a, b, c -> parameters
    print(a, b, c)


print_out(1, 2, 3)  # 1, 2, 3 -> arguments
print_out(4, 5, 6)

def salutation(name='No name'):
    print(f'Hello, {name}.')

salutation('Lucas Tenesse')
salutation()
