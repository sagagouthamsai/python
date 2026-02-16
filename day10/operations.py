#operators are used to perform operations on variables and values
#in python there are different types of operators

# 1.arithemetic operators it is used to perform mathematical operations on numbers
a = 5
b = 2

print("a + b =", a + b) #addition
print("a - b =", a - b) #subtraction
print("a * b =", a * b) #multiplication
print("a / b =", a / b) #division  This only gives the quotient
print("a // b =", a // b) #floor_division  This gives the quotient without the decimal part
print("a % b =", a % b) #modulus  This gives the remainder
print("a ** b =", a ** b) #exponentiation

# 2.assignment operators it is used to assign values to variables
x = 10
x += 5  # x = x + 5
print(x)
x -= 3  # x = x - 3
print(x)
x *= 2  # x = x * 2
print(x)
x /= 4  # x = x / 4
print(x)
x //= 2  # x = x // 2
print(x)
x %= 3  # x = x % 3
print(x)
x **= 2  # x = x ** 2
print(x)

# 3.comparison operators it is used to compare two values and returns a boolean value
print(a == b) #equal to
print(a != b) #not equal to
print(a > b)  #greater than
print(a < b)  #less than
print(a >= b) #greater than or equal to
print(a <= b) #less than or equal to

# 4.logical operators it is used to combine conditional statements
x = True
y = False
print(x and y) #logical AND  if both are true then it returns true otherwise it returns false
print(x or y)  #logical OR   if one of them is true then it returns true 
print(not x)   #logical NOT  if x is true then it returns false, vice versa
print(not y)   #logical NOT

# 5.identity operators it is used to compare the memory location of two objects
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)      # checks if both variables refer to the same object in memory
print(a is not b)  # checks if both variables refer to different objects in memory
print(a is c)      # checks if both variables refer to the same object in memory
print(a is not c)  # checks if both variables refer to different objects in memory

# 6.membership operators it is used to test if a sequence is present in an object
x = [1, 2, 3, 4, 5]
print(3 in x)  # checks if 3 is present in the list x
print(6 in x)  # checks if 6 is present in the list x
print(3 not in x)  # checks if 3 is not present in the list x
print(6 not in x)  # checks if 6 is not present in the list x

# 7.bitwise operators it is used to perform bitwise operations on integers
a = 5  # in binary: 0101
b = 3  # in binary: 0011
print(a & b)  # bitwise AND  (0101 & 0011 = 0001) 1
print(a | b)  # bitwise OR   (0101 | 0011 = 0111) 7
print(a ^ b)  # bitwise XOR  (0101 ^ 0011 = 0110) 6
print(~a)     # bitwise NOT  (~0101 = 1010) -6
print(a << 1) # left shift    (0101 << 1 = 1010) 10
print(a >> 1) # right shift   (0101 >> 1 = 0010) 2  





