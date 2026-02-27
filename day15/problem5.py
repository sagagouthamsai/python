#Remove duplicate characters
str="banana"
single_char=""
for i in str:
    if i in single_char:
        continue
    else:
        single_char+=i
print(single_char)