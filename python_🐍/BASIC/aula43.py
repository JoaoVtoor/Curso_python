# saved_password = '123456'
# entered_password = ''
# repetition = 0

# while saved_password != entered_password:
#     entered_password = input (f'Your password ({repetition}x): ')

#     repetition += 1

# print(repetition)
# print('This while can have infinite repetitions')
text = 'Python'

new_text = ''
for letter in text:
    new_text += f'*{letter}'
    print(letter)

print(new_text)