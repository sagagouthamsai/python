#other than update there are several ways to add sets
#union
set1={1,2,3,4}
set2={3,4,5,6,7}
set3={8,9,1,2,3}

#we can use union method or |
#an union always returns new set,update returns the modified set
#union can even join other datatypes also
print(set1.union(set2))
print(set1|set2)

#joining multiple sets
print(set1.union(set2,set3))

#intersection
#we can use intersection method or &
#intersection cannot add other data types
print(set1.intersection(set2))

#intersection_update()
#this will change the original set instead of returning a new set
set3.intersection_update(set1)
print(set3)

#difference()
#we can also use "-"
#this is used to find the different elements in sets
#this always give returns the unque elements from the first set 
print(set1.difference(set2))

#difference_update()
#this updates the first comparing set
print(set3-set2)
print(set3,"before")
set3.difference_update(set2)
print(set3,"set3 after difference_update")

#symmetric_difference()
##it gives unique values from both sets
#this and more two sided approach of difference method
#we can use ^
print(set1^set2)

#symmetric_differeence_update()
#this update the first comparision set
print(set1,"before")
set1.symmetric_difference_update(set2)
print(set1,"after symmetric_difference_update")

