# check even or odd for the given number using functions
def even_check(num):
    if num % 2 == 0:
        return True
    else:
        return False

# check odd
def odd_check(num):
    if num % 2 != 0:
        return True
    else:
        return False

print(even_check(10))
print(odd_check(10))