"""
Introduction to try/except
try -> try running the code
except -> an error occurred when trying to run
"""
number_str = input('Type a number: ')


try:
    number_float = float(number_str)
    print('FLOAT: ', number_float)
    print(f'The double of the number {number_str} is {number_float * 2:.2f}')
except:
    print('This is not a number')

if number_str.isdigit():
    number_float = float(number_str)
    print(f'The double of the number {number_str} is {number_float * 2:.2f}')
else:
    print('This is not a number')