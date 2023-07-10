"""
Exercise
Ask the user to type his name
Ask the user to type his age
If name and age are typed:
    Show:
        Your name is {name}
        Your name in reverse is {reverse name}
        If the name (has or not) spaces
        Your name has {n} letters
        The first letter of your name is {letter}
        The last letter of your name is {letter}
If nothing was typed in age or name
    Show:
        "Sorry, you left empty fields"
"""

name = input("Type your name: ")
age = input("Type your age: ")

if name and age:
    print(f'Your name is {name}.')
    print(f'Your in reverse is {name[::-1]}.')
    if ' ' in name:
        print('Your name has spaces ')
    else:
        print('Your name doesnt have spaces')
    print(f'Your name has {len(name)} letters')
    print(f'The first letter of your name is {name[0]}.')
    print(f'The last letter of your name is {name[-1]}.')
else:
    print('Sorry, you left empty fields')




