#Take two numbers and print:
#1. sum
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("Sum: ", a+b)
#2. difference
print("Difference: ", a-b)
#3. product
print("Product: ", a*b)
#4. quotient
print("Quotient: ", a/b)
#5. remainder
print("Remainder: ", a%b)
#6. power
print("Power: ", a**b)

#Check if a number is even or odd using %.
num=int(input("Enter a number: "))
if num%2==0:
    print(num, "is even.") 
else:    
    print(num, "is odd.")

#Take two numbers and print largest using comparison operators.
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
if num1>num2:
    print(num1, "is larger than", num2)
else:
    print(num2, "is larger than", num1)

#Check if a number is positive, negative, or zero.
num=int(input("Enter a number: "))
if num>0:
    print(num, "is positive.")
elif num<0:
    print(num, "is negative.")
else:
    print(num, "is zero.")

#Check if a number is divisible by both 3 and 5.
num=int(input("Enter a number: "))
if num%3==0 and num%5==0:
    print(num, "is divisible by both 3 and 5.")
else:
    print(num, "is not divisible by both 3 and 5.")

#Check if a number lies between 10 and 50 (inclusive).
num=int(input("Enter a number: "))
if num>=10 and num<=50:
    print(num, "lies between 10 and 50 (inclusive).")
else:
    print(num, "does not lie between 10 and 50 (inclusive).")

#Check if a character is a vowel using in operator.
char=input("Enter a character: ")
if char in 'aeiouAEIOU':
    print(char, "is a vowel.")
else:
    print(char, "is not a vowel.")

#Given 3 numbers, check if all are equal using logical operators.
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
if num1==num2 and num2==num3:
    print("all numbers are equal.")
else:
    print("Not all numbers are equal.")

#Check if a year is leap year using logical operators.
year=int(input("Enter a year: "))
if (year%4==0) and (year%100!=0) or (year%400==0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

#Check if a number is 2-digit AND even.
num=int(input("Enter a number: "))
if num>=10 and num<=99 and num%2==0:
    print(num, "is a 2-digit even number.")
else:
    print(num, "is not a 2-digit even number.")

#Swap two numbers without using third variable.
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print("Before swapping: num1 =", num1, "num2 =", num2)
num1=num1+num2
num2=num1-num2
num1=num1-num2
print("After swapping: num1 =", num1, "num2 =", num2)

#Find square and cube of a number using **.
num=int(input("Enter a number: "))
print("Square: ", num**2)
print("Cube: ", num**3)

#Evaluate expression:
x = 10
y = 5
z = 2
result = x + y * z ** 2
print("Result of x + y * z ** 2:", result)

#Predict output:
print(5 > 3 and 10 < 20 or 2 > 8)

#Predict output:
a = 5
b = 10
print(not(a > b))

#Check if "p" exists in "python" using membership operator.
if "p" in "python":
    print("'p' exists in 'python'.")
else:
    print("'p' does not exist in 'python'.")

#Compare two lists using == and is. Explain difference.

#== is used to check if two entities are equal in value
#is is used to check if two entities are the same object in memory


#Predict output:

a = [1,2,3]
b = [1,2,3]
print(a == b)
print(a is b)


#Check if a number exists in list [10,20,30,40].
num=int(input("Enter a number: "))
if num in [10,20,30,40]:
    print(num, "exists in the list.")
else:
    print(num, "does not exist in the list.")

#Predict:

x = None
print(x is None)

#Find 5 & 3, 5 | 3, 5 ^ 3.
print("5 & 3:", 5 & 3)
print("5 | 3:", 5 | 3)  
print("5 ^ 3:", 5 ^ 3)

#Without using %, check even/odd
num=int(input("Enter a number: "))
if num//2 != 0:
    print(num, "is even.")
else:
    print(num, "is odd.")

#Without using +, add two numbers
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
sum=num1-num2*(-1)
print("Sum:", sum)

#Find sign of number using operators only
num=int(input("Enter a number: "))
if num > 0:
    print("Sign of", num, "is +")
elif num < 0:
    print("Sign of", num, "is -")
else:
    print("Sign of", num, "is 0")

#Check if character is alphabet using operators
char=input("Enter a character: ")
if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
    print(char, "is an alphabet.")
else:
    print(char, "is not an alphabet.")

#Find maximum of 4 numbers using operators only
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
num4=int(input("Enter fourth number: "))
max_num=num1
if num2 > max_num:
    max_num = num2
if num3 > max_num:
    max_num = num3
if num4 > max_num:
    max_num = num4
print("Maximum number is:", max_num)
