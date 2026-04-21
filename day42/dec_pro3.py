def check_positive(func):
    def wrapper(*args,**kwargs):
        if args[0]%2!=0:
            print("invalid input")
            return
        
        res=func(*args,**kwargs)
        return res
    return wrapper

@check_positive
def square(n):
    return n * n

print(square(6))