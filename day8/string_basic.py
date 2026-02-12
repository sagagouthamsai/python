# an string is an sequence of characters that are presented inside qoutes (single, double or triple)
string="Hello World"
print(string)
print(type(string))

#single quotes
string1='Hello World'
#double quotes
string2="Hello World"
#triple quotes
string3='''Hello World'''

#multiline string
string4='''Hello

World'''
print(string4)

#accessing string
#we use indexing to access the elements in the string
#indexing starts from 0
#for indexing we use square brackets []
print(string[1])  
print(string[6])  

#we can use negative indexing also i.e. reverse indexing
print(string[-1]) 

#for accessing elements in string we can use for loop
for ele in string:
    print(ele)
#like we are looping an condition around string that goes through each element in the string and print it

#slicing
#slicing is an process of extracting a portion of the string using start and end index
#slicing syntax: string[start:end:step]   
print(string[0:5])  # prints "Hello" start=0,end=5
print(string[6:])   # prints "World" start=6,end of string
print(string[:5])   # prints "Hello" ":" this indicates we are intiating the indexing from start ,end=5
print(string[::2])  # prints every second character step=2

#the colon ":" is used to specify the start and end index for slicing
#like if its in start it will continue till the condition on the other end
str="Python is a great language"
print(str[:6]) 
print(str[7:])
print(str[::])
print(str[:])

#string reversal
print(str[::-1])  
