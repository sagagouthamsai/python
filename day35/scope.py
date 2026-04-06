#scope
#it is the region of the program where a variable is defined and can be accessed
#there are mainly four types of scope in python: local, enclosing(nested functions), global, and nonlocal

#local scope: variables defined inside a function and can only be accessed within that function
#enclosing scope: variables defined in the enclosing function and can be accessed within the nested function
#global scope: variables defined at the top level of the module and can be accessed throughout the module
#nonlocal scope: variables defined in the enclosing function and can be accessed within the nested function

#local scope example
def inner():
    x=20
    print(x,"local variable")
inner()
print(x)

#enclosing scope example
def outer():
    x = 10 
    print(x,"global variable")
    def inner():
        print(x,"enclosing variable")
    inner()

#global scope example
x = 30
def func():
    print(x,"global variable")
func()

#nonlocal scope example
#nonlocal variables are used to modify the variable defined in the nested function
def outer():
    x = 10 
    print(x,"global variable")
    def inner():
        nonlocal x
        x = 20
        print(x,"enclosing variable")
    inner()
    print(x,"after modification in inner function")

#global keyword is used to modify the variable defined in the global scope
x = 30
def func():
    global x
    x = 40
    print(x,"global variable")
func()