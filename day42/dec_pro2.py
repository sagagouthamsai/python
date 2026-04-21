def check_positive(func):
    def wrapper(n):
        if n<0:
            print("invalid input")
        return n
    return wrapper

@check_positive
def square(n):
    return n * n

print(square(-5))
