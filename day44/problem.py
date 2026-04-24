a="av bc"
l=a.split(" ")
res=[]
for words in l:
    res.append(words.capitalize())
print(' '.join(res))


#2nd approach
print(a.title())