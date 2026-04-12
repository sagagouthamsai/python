#decorators are used to modify the behavior of a function without changing its code.

def decorator(func
            ):
    def wrapper(a, b):
        return func(a, b) * 2
    return wrapper


@decorator
def add(a, b):
    return a + b

print(add(1,2))