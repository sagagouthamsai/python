#Create a decorator that counts how many times a function is called.
def func_call_count(func):
    count=0
    def wrapper(*args,**kwargs):
        nonlocal count
        count+=1
        res=func(*args,**kwargs)
        print("The function call count : ",count)
        return res
    return wrapper


@func_call_count
def add(*args):
    return sum(args)



print(add(1,2))
