"""
Make a game for the user to guess the secret word.
- You will propose any secret word and will give the possibility for the user to type only one letter.
- When the user types a letter, you will check if the typed letter is in the secret word.
    - If the typed letter is in the secret word; display the letter;
    - If the typed letter is not in the secret word; display *.
Count your user attempts.
"""
import os

word = 'tenesse'
correct_letter = ''
trys = 0

### Start
while True:
### Inputs
    letter_input = input('Type an letter: ')
    trys += 1
    if len(letter_input) > 1:
        print('Type only one letter.')
        continue

### Logic
    if letter_input in word:
        correct_letter += letter_input

    formed_word = ''
    for secret_letter in word:
        if secret_letter in correct_letter:
            formed_word += secret_letter
        else:
            formed_word += '*'
    print('Formed word: ', formed_word)

### End
    if formed_word == word:
        os.system('cls')
        print('You won.')
        print('The secret word was:',word)
        print('Trys:',trys)

### Reset
        correct_letter = ''
        trys = 0




