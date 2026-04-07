#arguments are baasically the values that we pass to a function during function call
#there are maninly three types of arguments
#1. positional arguments: these are the arguments that are passed to a function in the correct positional order
#2. keyword arguments: these are the arguments that are passed to a function with the help of the parameter name
#3. default arguments: these are the arguments that are given a default value in the function

#args
#this allows us pass n number of arguments in a function
def add(*numbers):
    print(sum(numbers)/len(numbers))
add(1, 2, 3)

#kargs
#this allows us to pass multiple dict arguments
