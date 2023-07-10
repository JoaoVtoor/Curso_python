"""
Calculation of the first digit of the CPF
CPF: 746.824.890-70
Collect the sum of the first 9 digits of the CPF
multiplying each of the values by a
countdown starting from 10

Ex.: 746.824.890-70 (746824890)
   10 9 8 7 6 5 4 3 2
* 7 4 6 8 2 4 8 9 0
   70 36 48 56 12 20 32 27 0

Sum all results:
70+36+48+56+12+20+32+27+0 = 301
Multiply the previous result by 10
301 * 10 = 3010
Get the remainder by dividing the previous count by 11
3010% 11 = 7
If the previous result is greater than 9:
    result is 0
contrary to this:
    result is the account value

The first digit of the CPF is 7
"""
cpf = '74682489070'
nine_digit = cpf[:9]
i = 10

result_digit_1 = 0
for digit_1 in nine_digit:
    result_digit_1 += int(digit_1) * i
    i -= 1
digit_1 = (result_digit_1 * 10 % 11)
digit_1 = digit_1 if digit_1 <= 9 else 0
print(digit_1)