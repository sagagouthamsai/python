#Write a function to add two numbers
def add(a,b):
    print(a+b)

add(2,3)

#Write a function to check even or odd
def even_check(n):
    if n%2==0:
        print("even")
    else:
        print("odd")

even_check(2)

#Write a function to find the square of a number
def square(a):
    print(a**2)
square(10)

#Function to find maximum of two numbers
def max(num1,num2):
    if num1>num2:
        print(f"{num1} is greater than {num2}")
    else:
        print(f"{num2} is greater than {num1}")
max(17,23)

#Function to count characters in a string
def string_count(string):
    count=0
    for i in string:
        count+=1
    print(count)
string_count("abdc")

#Function to check if number is positive, negative, or zero
def num_expression_check(number):
    if number>0:
        print(f"{number} is positive")
    elif number<0:
        print(f"{number} is negative")
    else:
        print(f"{number} is zero")
num_expression_check(-1)

#Function to reverse a string
def reverse_str(string):
    print(string[::-1])
reverse_str("listen")

#Function to calculate factorial
def factorial(number):
    n=1
    for i in range(1,number+1):
        n*=i
    print(n)
factorial(5)