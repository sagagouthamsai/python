#Write a program to remove duplicate values from a list using sets.
Input_value = [1,2,2,3,4,4,5,6,6]
print(set(Input_value))

#Write a program to find common elements in three sets.
set1={1,2,3,4,5}
set2={3,4,5,6,7}
set3={4,5,6,7,8}

print(set1.intersection(set2,set3))

#Write a program to find pairs of numbers whose sum equals a target using sets.
List_value=[1,2,3,4,5]
convo_set=set(List_value)
print(convo_set)
pairs=set()
for i in convo_set:
    for j in convo_set:
        if (i+j)==6:
          pairs.add((i,j))
        else :
           continue  
print(pairs)

#Write a program to determine whether two lists contain the same elements regardless of order.

ab=[1,2,3]
bc=[3,2,1]
AB=set(ab)
BC=set(bc)

if AB==BC:
   print("yes")
else:
   print("no")

#Write a program to find first repeated element in a list using sets.
list1=[1,2,3,3,4,5,6]
seen=set()
for ele in list1:
   if ele in seen:
      print(ele)
   seen.add(ele)




