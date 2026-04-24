def int_only(func):
    def int_check(*args,**kwargs):
        for value in args:
            if not isinstance(value,int):
                print("Only integers allowed")
                return
        return func(*args,**kwargs)
    return int_check 


@int_only
def add(a, b):
    return a + b

print(add(2, 3))
print(add(2, "x"))