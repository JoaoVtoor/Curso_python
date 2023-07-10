import random

#  Generating random CPF

for _ in range(100):
    #  First Digit
    nine_digit = ''
    for i in range(9):
        nine_digit += str(random.randint(0,9))

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
    digit_3 = str(digit_1) + str(digit_2)

    new_cpf = '{}.{}.{}-{}'.format(nine_digit[:3], nine_digit[3:6], nine_digit[6:9], digit_3)

    print(f'CPF: {new_cpf}')