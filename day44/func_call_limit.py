def limit_calls(func):
    count=0
    def count_check(*args,**kwargs):
        nonlocal count
        if count>=2:
            print("Limit reached")
            return
        count+=1
        print("The function name is ",func.__name__)
        return func(*args,**kwargs)
    return count_check

@limit_calls
def test():
    print("Running")

test()
test()
test()