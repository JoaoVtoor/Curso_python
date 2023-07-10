"""
Flag - mark a location
None - non value
is and is not (identity, value, type)
id - identity
"""
v1 = 'a'
v2 = 'a'
print(id(v1))
print(id(v2))

condition = True
pass_if = None

if condition:
    pass_if = True
    print('Do something')
else:
    print('Dont do something')

if pass_if is None:
    print('Not passed in the if')

if pass_if is not None:
    print('Passed the if')