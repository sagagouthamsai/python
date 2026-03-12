#sets are unordered ,mutable ,unique and created using {}
#sets have unique elements and duplication is not allowed,it implesitly removes duplicates
#after creation an elment can be modified,can be removed or added
#in set every time we access them it returns an different output

#set creation
example_set={1,2,3,"apple"}
print(example_set)

#duplicate sets
duplicate_set={"apple",1,2,3,1,2,3,"banana"}
print(duplicate_set)

#empty set creation
#for empty set creation we use set() because using {} creates dictionaries
set1={}
print(type(set1))
set2=set()
print(type(set2))

#accessing sets
#sets cannot be accesed by index as they are unorderd so we use looping or membeship operators
for ele in example_set:
    print(ele)

if 1 in example_set:
    print("yes")
else:
    print("no")

