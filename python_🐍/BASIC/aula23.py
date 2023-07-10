# Logic Operator "not"
# used to reverse expressions
# not True = False
# not False = True
print(not True) # False
print(not False) # True

password = input('Password: ')

if not password:
    print('Incorrect Password')