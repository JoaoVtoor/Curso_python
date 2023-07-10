"""
Scope of python functions
Scope means the place where that code can reach.
There's the global and local scope.
The global scope is the scope where all the code is reachable.
The local scope is the scope where only names from the same location
can be reached.
We dont have acess to inner scope names in outer scopes.
The word global makes a variable in the outer scope
the same as in the inner scope.
"""

x = 1

def scope():
    global x
    x = 10

    def function():
        global x
        x = 11
        y = 2
        print(x, y)

    function()
    print(x)

print(x)
scope()
print(x)