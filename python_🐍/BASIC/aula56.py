"""
split and join with list/str
split -> divides an string
join -> unites an string
"""
phrase = '   Hello,   thats interesting.   '
list_phrases_fixed = phrase.split(',')

list_phrases = []
for i, phrase in enumerate(list_phrases_fixed):
    list_phrases.append(list_phrases_fixed[i].strip())  # r/l/strip() -> removes spaces

print(list_phrases_fixed)
print(list_phrases)

united_phrases = '-'.join(list_phrases)
print(united_phrases)