#an deccorator is an function which uses another or modifies an function behavior without changing the original function
#basic DECORATOR  syntax:

def decorator(fun):
    def wrapper():
        fun()
        print("this is a wrapper function")
    return wrapper
@decorator
def display():
    print("this is a display function")

display()