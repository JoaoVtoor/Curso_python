# "in" and "not in"
# Strings are iterable
#  0 1 2 3 4 5
#  R o b e r t
# -6-5-4-3-2-1
name = 'Robert'

print(name[2])
print(name[-4])
print('-'*10)
print('e' in name)
print('z' not in name)

name2 = input('Type your name: ')
find = input('Type what you want to find: ')

if find in name2:
    print(f'{find} is in {name2}')
else:
    print(f'{find} is not in {name2}')