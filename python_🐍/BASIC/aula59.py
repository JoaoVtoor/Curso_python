"""
Unpacking method
and function calls
"""
str = 'ABCD'
list_a = ['Lucas', 'Tenesse', 1, 2, 3, 'John']
tuple_a = 'Python', 'is', 'goofy'
rooms = [
    # 0        1
    ['Lucas', 'Tenesse', ],  # room0
    # 0
    ['Elaine', ],  # room1
    # 0        1       2
    ['Luiz', 'Thomas', 'John', (0, 10, 20, 30, 40)],  # room2
]

first, b, c, *_, d,last = list_a
print(first, d, last)

# for name in list_a:
#     print(name, end=' ') #  end= ' ' -> 1 line
# print(*list_a)
# print(*str)
# print(*tuple_a)

print(*rooms, sep='\n')