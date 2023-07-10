"""
Make a shopping list with lists
The user must be able to insert, delete and 
list values from his list
Don't allow the program to break with errors for non-existent 
indexes in the list.
"""
import os

list_a = []
while True:
    print('Selecione uma opção:')
    option = input('[i]nsert [d]elete [l]ist:')

    if option == 'i':
        os.system('cls')
        value = input('Valor: ')
        list_a.append(value)

    elif option == 'l':
        os.system('cls')
        if len(list_a) == 0:
            print('Nothing to list')

        for i, value in enumerate(list_a):
            print(i, value)

    elif option == 'd':
        os.system('cls')
        index = input('Choose the index to delete: ')
        try:
            index = int(index)
            del list_a[index]
        except ValueError:
            print('Please type an integer.')
        except IndexError:
            print('Index does not exist.')
        except Exception:
            print('Unknown error')

    else:
        print('Please, select an option')

