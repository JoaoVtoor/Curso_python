phrase = 'Python is a programming language ' \
    'multiparadigm. ' \
    'Python was created by Guido van Rossum.'

i = 0
most_appeared = 0
letter_most_appered = ''

while i < len(phrase):
    current_letter = phrase[i]

    if current_letter == ' ':
        i += 1
        continue

    current_most_appeared = phrase.count(current_letter)
    if most_appeared < current_most_appeared :
        most_appeared = current_most_appeared
        letter_most_appered = current_letter

    i += 1

print(f'The most appeared letter was "{letter_most_appered}"'\
      f' and it appeared {most_appeared}x'
)