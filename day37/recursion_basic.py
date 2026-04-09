#recursion 
#recursion is a function that calls itself
#it is a way to solve problems by breaking them down into smaller, more manageable pieces
#in recursion we need a base case and a recursive case
#the base case will stop the recursion

#recursive function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5)) 

#recursive function to calculate the nth Fibonacci number
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))


