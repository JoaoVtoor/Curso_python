"""
Repetition
while
Performs an action while the condition is true
"""
line_qty = 5
col_qty = 5

line = 1
while line <= line_qty:
    column = 1
    while column <= col_qty:
        print(f'{line=} {column=}')
        column += 1
    
    line += 1

print('End')