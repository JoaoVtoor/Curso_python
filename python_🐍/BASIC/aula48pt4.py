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

list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_c = list_a + list_b
print(list_c, 'List C')
list_a.extend(list_b)
print(list_a, 'List A')