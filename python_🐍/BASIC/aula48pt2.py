"""
Lists in Python
type list - mutable
Supports multiple values of any type
Reusable knowledge - indexes and slicing
Useful methods: 
    append, insert, pop, del, clear, extend, +
Create  Read  Update  Delete
list[i] = CRUD
"""
#         0   1   2   3
lista = [10, 20, 30, 40] #  Create
# lista[2] = 300 #  Update
# del lista[3] #  Delete
# print(lista)
# print(lista[2]) #  Read

# append -> add a new element to the end of the list
lista.append(50)
lista.append(60)
lista.append(70)

# pop -> deletes the last element of the list
last_element = lista.pop(3)

print(lista, 'Removed:', last_element)