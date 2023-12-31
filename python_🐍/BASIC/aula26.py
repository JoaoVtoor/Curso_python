# Basic string formatting
# s - string
# d - int
# f - float
# .<number of digits>f
# x or X - Hexadecimal
# (Character)(><^)(quantity)
# > - Left
# < - Right
# ^ - Center
# Force the number to appear before the 0
# Sign - + or - 
# Ex.: 0>-100,.1f
# Conversion flags - !r !s !a

variable = 'ABC'
print(f'{variable}')
print(f'{variable: >10}')
print(f'{variable: <10}.')
print(f'{variable: ^10}.')
print(f'{1000.54353453:0=+10,.1f}')
print(f'The hexadecimal of 1500 is {1500:08X}')
print(f'{variable!r}')
