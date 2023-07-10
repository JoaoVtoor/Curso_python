"""
Careful with mutable data
= -> copied the value (imutable)
= -> points to the same value in memory (mutable)
"""
# name = 'Lucas'
# other_variable = name
# name = 'John'
# print(name)
# print(other_variable)

list_a = ['Lucas', 'Luiz', 1, True, 1.2]
list_b = list_a.copy()

list_a[0] = 'Anything'
print(list_a)
print(list_b)