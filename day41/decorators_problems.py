def my_decorator(fun):
    def wrapper():
        print("Function started")
        fun()
        print("Function ended")
    return wrapper

@my_decorator
def greet():
    print("Hello")

greet()


def decorator(fun):
    def wrapper(*args, **kwargs):
        print("Running function")
        res=fun(*args, **kwargs)
        return res
    return wrapper
@decorator
def add(a, b):
    return a + b

print(add(2, 3))


