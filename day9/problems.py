#Convert "python programming" → uppercase
a="python proogramming"
print(a.upper())
#Remove spaces from " hello world "
print(" hello world ".strip(" "))
print(" hello world ".replace(" ",""))
#Count how many "a" in "banana"
print("banana".count("a"))
#Replace "bad" with "good" in "bad boy"
print("bad boy".replace("bad","good"))
#Check if "12345" is digit
print("12345".isdigit())
#Medium
#Reverse words of "I love python"
str="I love python"
print(" ".join(str.split()[::-1]))
#Count vowels in input string
"""ip=input("enter an string : ")
count=0
for str in ip:
    if str in "aeiou":
        count+=1
print(count)"""

#Remove all "a" from "banana"
print("".join("banana".split("a")))

#Convert "hello world" → "HELLO-WORLD" using join()
print("-".join((("hello world".upper()).split(" "))))

#Print first non-repeating character in "aabbccdeff"
word="aabbccdeff"

for ch in word:
    if word.count(ch)==1:
        print(ch)
        



#Slight Interview Level
#Check if string is palindrome
#Count words in sentence
#Find largest word in sentence
#Remove duplicate characters from "programming"
#Convert "goutham sai" → "sai goutham" (without slicing reverse)