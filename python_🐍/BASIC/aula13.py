name = 'Lucas Tenesse'
height = 1.80
weight = 80

bmi = weight/(height * height)

#f-strings
line_1 = f'{name} is {height:.2f}m tall'
line_2 = f'weighs {weight}kg and his BMI is: {bmi:.2f}'

print(line_1)
print(line_2)