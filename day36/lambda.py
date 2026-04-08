#lambda functions are anonymous functions, meaning they do not have a name. 
# They are defined using the lambda keyword 
# it can take any number of arguments but can only have one expression. 
# The syntax for a lambda function is as follows:
# lambda arguments: expression

add = lambda x, y: x + y
print(add(5, 3))

# Lambda functions can also be used in higher-order functions like map(), filter(), and reduce().

#lambda with map()
#map() is an built-in function that applies a given function to each item of an iterable
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)

#lambda with filter()
#filter() is a built-in function that makes an iterator from elements in iterable for which a function returns true.
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

