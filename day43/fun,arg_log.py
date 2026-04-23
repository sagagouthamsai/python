def log_call(func):
    def wrapper(*args,**kwargs):
        print("Funtion_name : ",func.__name__)
        print("Arguments : ",args)
        return func(*args,**kwargs)
    return wrapper


@log_call
def multiply(a, b):
    return a * b

print("Result:", multiply(2, 3))