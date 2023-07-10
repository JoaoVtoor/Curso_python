"""
Calculation of the second digit of the CPF
CPF: 746.824.890-70
Collect the sum of the first 9 digits of the CPF
PLUS FIRST DIGIT,
multiplying each of the values by a
countdown starting from 11

Ex.: 746.824.890-70 (7468248907)
   11 10 9  8  7  6  5  4  3  2
*  7  4  6  8  2  4  8  9  0  7
   77 40 54 64 14 24 40 36 0 14

Sum all results:
77+40+54+64+14+24+36+0+14 = 363
Multiply the previous result by 10
363 * 10 = 3630
Get the remainder by dividing the previous count by 11
363% 11 = 0
If the previous result is greater than 9:
    result is 0
contrary to this:
    result is the account value

The first digit of the CPF is 7
The second digit of the CPF is 0
"""
import re
import sys

# cpf = '746.824.890-70' \
#     .replace('.','') \
#     .replace('-','') 
entry = input('CPF [746.824.890-70]: ')
cpf = re.sub(
    r'[^0-9]',
    '',
    entry
)


#  string -> ssssss
entry_is_repeated = entry == entry[0] * len(entry)

if entry_is_repeated:
    print('You sent repeated characteres')
    sys.exit()


#  First Digit
nine_digit = cpf[:9]
i = 10

result_digit_1 = 0
for digit_1 in nine_digit:
    result_digit_1 += int(digit_1) * i
    i -= 1
digit_1 = (result_digit_1 * 10 % 11)
digit_1 = digit_1 if digit_1 <= 9 else 0

#  Second Digit
ten_digit = nine_digit + str(digit_1)

j = 11
result_digit_2 = 0
for digit_2 in ten_digit:
    result_digit_2 += int(digit_2) * j
    j -= 1

digit_2 = (result_digit_2 * 10 % 11)
digit_2 = digit_2 if digit_2 <= 9 else 0

new_cpf = f'{nine_digit}{digit_1}{digit_2}'
if cpf == new_cpf:
    print(f'{new_cpf} is valid.')
else:
    print('Invalid.')