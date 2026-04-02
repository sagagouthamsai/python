#function types are basically divided into three types.
#in-built, user defined, higher order functions
#user-defined functions types continueation

#default arguments
def greet(default="user"):
    print(f"hello {default}")
greet(),greet("a")

#keyword arguments
def student(name, age):
    print(name, age)
student(age=20, name="Sai")

#Variable-Length Arguments
#args :this is used when we want to send n no.of numerical parameters
def total_sum(*numbers):
    return sum(numbers)
print(total_sum(1, 2, 3, 4))

#kargs :is another type of variable length arguments but it is used when we want to send n no.of keyword arguments
def student_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
student_info(name="Sai", age=20, city="Hyderabad")
