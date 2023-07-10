"""
Repetition
while
Performs an action while the condition is true
"""
counter = 0

while counter <= 100:
    counter += 1

    if counter % 2 == 1:
        continue

    print(counter)

    if counter == 40:
        break

print('end')