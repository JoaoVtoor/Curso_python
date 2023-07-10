"""
enumarete - enumaretes iterables (indexes)
"""
# [(0, 'Lucas'), (1, 'Tenesse'), (2, 'John'), (3, 'Thomas')]
list_a = ['Lucas', 'Tenesse', 'John']
list_a.append('Thomas')

# enumerated_list = list(enumerate(list_a, start=5))

for index, name in enumerate(list_a):
    print(index, name)

# for item in enumerate(list_a):
#     index, name = item
#     print(index, name)

# for item in enumerate(list_a):
#     print('FOR of tuple:')
#     for value in item:
#         print(f'\t{value}')