"""
Scope of python functions
Scope means the place where that code can reach.
There's the global and local scope.
The global scope is the scope where all the code is reachable.
The local scope is the scope where only names from the same location
can be reached.
"""
x = 1

def scope():
    global x
    x = 10

    def function_2():
        x = 15
        y = 2
        print(x, y)

    print(x)
    function_2()

print(x)
scope()
print(x)