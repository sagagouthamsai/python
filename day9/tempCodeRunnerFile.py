ip=input("enter an string : ")
count=0
for str in ip:
    if str in "aeiou":
        count+=1
print(count)