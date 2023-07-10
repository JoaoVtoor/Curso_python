"""
Lists in Python
type list - mutable
Supports multiple values of any type
Reusable knowledge - indexes and slicing
Useful methods - append, insert, pop, del, clear, extend, +
"""
#     +01234
#     -54321
string = 'ABCDE' # 5 characters (len)

# [], list(), '', falsy

#         0    1          2           3   4
#        -5   -4         -3          -2  -1
lista = [123, True, 'Lucas Tenesse', 1.2, []]
print(lista, type(lista))
print(lista[2], type(lista[2]))

lista[-3] = 3
print(lista[2], type(lista[2]))