"""
Write a program that asks the user to enter an integer,
inform if this number is even or odd. If the user does not enter a number
integer, inform that it is not an integer.
"""
number = input('Enter an number: ')

if number.isdigit():
    number_int = int(number)
    if number_int % 2 == 0:
        print('The number is even')
    else:
        print('The number is odd')
else:
    print('The number is not an interger')

"""
Write a program that asks the user for the time and, based on the time
described, display the appropriate salutation. Ex.
Good morning 0-11, Good afternoon 12-17 and Good evening 18-23.
"""
time = input('Type your time: ')
time_float = float(time)
time_aft = time_float > 11 and time_float <= 17
time_eve = time_float > 17 and time_float <= 23

if time_float <= 11:
    print(f'Good morning {time_float:.2f} ')
if time_aft:
    print(f'Good afternoon {time_float:.2f} ')
if time_eve:
    print(f'Good evening {time_float:.2f} ')

"""
Write a program that asks for the user's first name. If the name has 4 letters or
minus write "Your name is short"; if it has between 5 and 6 letters, write
"Your name is normal"; greater than 6 write "Your name is too long".
"""
name = input('Type your name: ')
len_med = len(name) >= 5 and len(name) <= 6
len_long = len(name) > 6

if len(name) <= 4:
    print(f'Your {name=} is short')
if len_med:
    print(f'Your {name=} is normal')
if len_long:
    print(f'Your {name=} is too long')