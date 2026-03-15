#Write a program to find common elements between two sets.
A={1,2,3,4}
B={3,5,6}
c={3,4,7,8}

print(A.intersection(B))

#Write a program to check whether one set is a subset of another.
if A.issubset(B):
    print("a is subbset of b")
elif B.issubset(A):
    print("B is subset of A")
else:
    print("no subsets found")

#Write a program to remove all elements from a set.
A.clear()
print(A)

#Convert a string "programming" into a set and print unique characters.
string_value="programming"
print(set(string_value))

#Write a program to find elements present in either set but not both.
unique=A.symmetric_difference(B)
print(unique)

#Write a program to find maximum and minimum values in a set without using max() or min().
set1={1,2,3,4,5,6,10,3,4,}
list_set=list(set1)
list_set.sort()
print(list_set[-1]," : max",'  ',list_set[0]," : min")



