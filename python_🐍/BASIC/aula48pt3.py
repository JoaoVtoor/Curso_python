"""
Lists in Python
type list - mutable
Supports multiple values of any type
Reusable knowledge - indexes and slicing
Useful methods: 
    append - Adds an item to the end
    insert - Adds an item to the chosen index
    pop - Removes from the end or the chosen index
    del - deletes an index
    clear - clear the list
    extend - extends the list
    + - concatenates lists
Create  Read  Update  Delete
list[i] = CRUD
"""
#         0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Lucas Tenesse')
name = lista.pop()
lista.append(1233)
del lista[-1] # -1 ->  always the last
# lista.clear()
lista.insert(100, 5) #  (index, object)
# print(lista[100]) -> Index out of range
print(lista, name)
