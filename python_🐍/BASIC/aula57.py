"""
Lists of lists and their indexes
"""
rooms = [
    # 0        1
    ['Lucas', 'Tenesse', ],  # room0
    # 0
    ['Elaine', ],  # room1
    # 0        1       2
    ['Luiz', 'Thomas', 'John', (0, 10, 20, 30, 40)],  # room2
]

# print(rooms)
# print(rooms[0][1])
# print(rooms[2][2])
# print(rooms[2][3][2])

for room in rooms:
    print(f'The room is: ')
    for student in enumerate(room):
        print(student)
