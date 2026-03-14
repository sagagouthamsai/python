# print a string "Hi I'm Bhavanidevi Btech ECE with 80%"
#fun(name="Bhavanidevi",course="Btech", branch="ECE", perc=80%)

"""
def info(name,course,branch,perc):
    print(f"hi I'am {name} pursuing my {course} {branch} with percentage : {perc}")

info("goutham","B-Tech","AI&DS",80)
print("end")
"""

"""
s=input("enter an string : ")
l= list(s.split())
a=[] 
for i in range (len(l)):
    cnt=0 
    for char in l[i]:
        if char.isalpha():
            cnt+=1 
    a.append(cnt)
print(a)
b=max(a)
index_value=a.index(b)
print(l[index_value])
"""

"""
find a string which is palindromic string without any in-built funtions 
string_value=input("enter any string : ")
split_string=string_value.split()
palindrome_container=" "
for words in split_string:
    if words[::-1]==words:
        palindrome_container+=words+" "

print(palindrome_container)
"""

"""
#take a list and str, count the vowels in them
list_value=list(input("enter elements of list : "))
str_value=str(input("enter the string : "))
print("Vowels in list")
for items in list_value:
    if items in "aeiouAEIOU":
        print(items)
print("Vowels in string")
for element in str_value:
    if element in "aeiouAEIOU":
        print(element)
"""

"""
input_value=input("Enter an list : ")
list_value=list(input_value.split(","))
unique_list=[]
print(list_value)
for item in list_value:
    if item not in unique_list:
        unique_list.append(item)
    else:
        continue
print(unique_list)

"""

