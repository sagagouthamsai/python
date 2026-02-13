#string methods are the built-in functions that are used to perform various operations on strings
#string methods are called using the dot operator (.)
string="hello world"

#upper method :it is used to convert the string to uppercase
print(string.upper())  

#lower method : it is used to convert the string to lowercase
print(string.lower())

#strip method : it removes whitespace from the beginning and end of the string
space= "   hello world   "
print(space.strip())

#in this there are two conditions 
#lstrip 
print(space.lstrip())

#rstrip
print(space.rstrip())

#string replace : it replaces string elements 
print(string.replace("world","Goutham"))

#string split:This splits the string when the given condition is meet
#returns the split elements in tempo list
print(string.split(" "))

#type-checking methods
s = "Python123 hello abc123"

print(s.isalpha())   
print(s.isdigit())   
print(s.isalnum())   
print(s.islower())   
print(s.isupper())   
print(s.startswith("Py")) 
print(s.endswith("123"))  
print(s.capitalize())
print(s.title())

#string functions
#len() function : it returns the length of the string
print(len(string))

#count() function : it returns the number of occurrences of a substring in the string
print(string.count("o"))

#find() function : it returns the index of the first occurrence of a substring in the string
print(string.find("world"))

#index() function : it returns the index of the first occurrence of a substring in the string
print(string.index("world"))

print(max(string))  # returns the maximum character in the string

print(min(string))  # returns the minimum character in the string








