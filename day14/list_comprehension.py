#list comprehension is a complex yet powerful way to create looped lists in a single line of code
#every time list comprehension is used, it creates a new list and fills it with the values returned by the expression
#example : create a list of squares of numbers from 0 to 9

#syntax : [expression for item in iterable if condition]
squares = [x**2 for x in range(10)]
print(squares)

#filtering items in list comprehension
#list comprehension if condition is optional, but it can be used to filter the items in the iterable
#example : create a list of squares of even numbers from 0 to 9

#syntax : [expression for item in iterable if condition]
even_squares = [x**2 for x in range(10) if x%2==0]
print(even_squares)


