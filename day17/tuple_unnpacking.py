#tuple unpacking
#it is an way to assign values in the tuple to an variable 

tupl= ("apple", "banana", "cherry")
(green, yellow, red) = tupl
print(green)
print(yellow)
print(red)

#if no.of variables is less than no.of values then we use astarisk to assign remaining values
#every value must be assigned to a variable, if not we get an error
#we can also use the astarisk to assign values to a variable as a list
tupl = ("apple", "banana", "cherry", "grapes", "kiwi")
(green, yellow, *red) = tupl
print(green)
print(yellow)
print(red)


