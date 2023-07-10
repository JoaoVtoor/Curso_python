# Basic string interpolation
# s -> string
# d and i -> int
# f -> float
# x e X -> Hexadecimal (ABCDEF0123456789)

name = 'Lucas'
price = 1000.95897643
variable = '%s the price is $%.2f' % (name, price)
print(variable)

print('The hexadecimal of %d is %04x' % (1500, 1500))