#program to print n natural numbers using recursion
def n_print(n):
    if n > 0:
        n_print(n-1)
        print(n)
    

def rev_str(str):
    return str[::-1]

print(rev_str("hello"))
n_print(10)

def revstr(str):
   
    if len(str) == 0:
        return str
    else:
        return revstr(str[1:]) + str[0]
print(revstr("hello"))

