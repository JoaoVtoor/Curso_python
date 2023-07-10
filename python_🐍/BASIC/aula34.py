"""
Repetition
while
Performs an action while the condition is true
"""

condition = True
while condition:
    name = input('Whats your name: ')
    print(f'Your name is {name}')
    
    if name == 'Leave':
        break

print('End')