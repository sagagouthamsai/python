
#global and local variables
x = 10  # global variable

def print_values():
    y = 20  
    print(x)
    print(y)
print_values()
print(x)

#an global variable can be accessed throughout
#But a local variable can only be accessed within the function where it is defined.

#to modify a global variable inside a function, we need to use the 'global' keyword
def modify_global():
    global x
    x = 20  
modify_global()
print(x)  

#nonlocal is used to modify a local variable via another function
def outer():
    x = 10  
    def inner():
        nonlocal x  
        x = 20  
    inner()
print(x)


