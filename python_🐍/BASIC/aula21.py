# Logic operators
# and or not
# and -> All conditions must be true
# If any value is considered false
# the entire expression will evaluate to that value
# Are considered falsy: 
# 0 0.0 '' False
# Also 'None' is used to represent a non-value

entry = input('[E] Enter [L] Leave ')
password = input('Password: ')
permited_password = '123456'

#if True:
if entry == 'E' and password == permited_password:
    print('Entered')
else:
    print('Left')

# Short Circuit Evaluation
print(True and False and True)