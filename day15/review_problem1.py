#revesing string with out [::-1]
str ="goutham"
rev = ""
pos=-1
for ele in range (len(str)):
    rev+=str[pos]
    pos=pos-1
    
print(rev)