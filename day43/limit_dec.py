def limit_args(func):
    def wrapper(*args):
        if len(args)>3:
            print("too many arguments")
            return
      
        return(func(*args))
    return wrapper
        


@limit_args
def add(a, b, c):
    return a + b + c

print(add(1, 2, 3))
print(add(1, 2, 3, 4))