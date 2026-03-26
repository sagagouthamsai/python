#Count how many numbers are divisible by 3
for num in range(1,31):
    if num%3==0:
        print(num)
    else:
        continue

#Find the largest number in a list
num_list=[1,2,3,4,5,5,6,7,8,1,2,5,9,1,4,2]
max=0
for max_num in num_list:
    if max_num>max:
        max=max_num
print(max)

#Count vowels in a string
string1="programming"
vowel_count=0
for char in string1:
    if char in "aeiouAEIOU":
        vowel_count+=1
print(vowel_count)

#print the right triangle pattern
for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print()

#Find factorial of a number
n=5
m=1
for i in range(1,n+1):
    m=m*i
print(m)

