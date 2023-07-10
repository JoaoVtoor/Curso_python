"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Immutables: str, int, float, bool
"""

string = 'lucas Tenesse'
a = f'{string[:3]}ABC{string[4:]}'
print(string)
print(a)
print(string.capitalize())
print(string.zfill(15))