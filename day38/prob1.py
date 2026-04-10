def exe(n):
    for i in range(n):
        yield i

def div3(n):
    for i in range(n):
        if i%3==0:
            yield i

a=exe(100)
for i in range(1,100):
    print(next(a))

b=div3(100)
print("Divisible by 3:")
for i in b:
    print(i)

