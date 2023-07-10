"""
Calculator with while
"""
while True:
### Inputs
    num_1 = input('First number: ')
    num_2 = input('Second number: ')
    operator = input('Select an operator [+][-][/][*] ')

### Validation
    valid_num = None
    num_1_float = 0
    num_2_float = 0
    try:
        num_1_float = (float(num_1))
        num_2_float = (float(num_2))
        valid_num = True
    except:
        valid_num = None

    if valid_num is None:
        print('The numbers are not valid.')
        continue

    valid_operators = '+-/*'
    if operator not in valid_operators:
        print('Invalid Operator.')
        continue

    if len(operator) > 1:
        print('Select only one operator.')
        continue

### Calculator
    print('Calculating.... Result:')
    if operator == '+':
        print(f'{num_1_float} + {num_2_float} =', num_1_float + num_2_float)
    elif operator == '-':
        print(f'{num_1_float} - {num_2_float} =', num_1_float - num_2_float)
    elif operator == '/':
        print(f'{num_1_float} / {num_2_float} =', num_1_float / num_2_float)
    elif operator == '*':
        print(f'{num_1_float} * {num_2_float} =', num_1_float * num_2_float)
    else:
        print('unknown error')

### Leave Script
    leave = input('Leave? [y]es: ').lower().startswith('y')
    if leave is True:
        print('end')
        break