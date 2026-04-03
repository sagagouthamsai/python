#positional arguments
#the position of the arguments matters when calling the function
#the first argument will be assigned to the first parameter and second argument to second parameter
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet("Alice", 30)

#priority is given to positional arguments first then default
#positional>default>args>keyword>kargs 
   