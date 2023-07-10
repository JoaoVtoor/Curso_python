"""
Exercise
Show the indexes of the list
"""
list_a = ['Lucas', 'Tenesse', 'John']
list_a.append('Thomas')
indexes = range(len(list_a))

for index in indexes:
    print(index, list_a[index], type(list_a[index]))
