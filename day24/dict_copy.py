#to make an copy of the dict we use copy()
example_dict={'type' : 'fruit', 'name' : 'apple','color':'red'}
mydict = example_dict.copy()
print(mydict)

#we can also use dict() constructor to copy dict elements
mydict1=dict(example_dict)
print(mydict1)