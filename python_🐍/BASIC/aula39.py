"""
String iteration with while
"""
#       0123456789101112
name = 'Lucas Tenesse' # Iteratable
#   13121110987654321

n = 0
new_name = ''
while n < len(name):
    letter = name[n]
    new_name += f'*{letter}'
    n += 1

print(new_name)
