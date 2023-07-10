"""
Iterable -> str, range ... (__iter__)
Iterator -> delivers an value at a time
next -> hand me the next value
iter -> hand me your iterator
"""
# text = iter('Lucas') # __iter__()

# print(next(text)) # __next__()
# print(next(text))
# print(next(text))
# print(next(text))
# print(next(text)) # StopIteration


# for letter in text
text = 'Lucas' # itarable
iterator = iter(text) # iterator
while True:
    try:
        letter = next(iterator)
        print(letter)
    except StopIteration:
        break
# end of for