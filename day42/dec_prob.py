def log_call(func):
    def wrapper(*args,**kwags):
        print("Calling function")
        func()
    return wrapper
@log_call
def greet():
    print("Hello")

greet()