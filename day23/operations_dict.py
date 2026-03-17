#for adding an element in dictionary we can use indexing or update() function.

#addition using indexing
#syntax dict_name[key]=value
example_dict={"name":"goutham","age":19}
example_dict["year"]=2026
print(example_dict)

#addition using update().
#the update() function uses an internal dict to add
example_dict.update({"date":"3-17-2026"})
print(example_dict)

#removing dict
#we use pop() or popitem()
example_dict.pop("date")
print(example_dict)

example_dict.popitem()
print(example_dict)

#del keyword deletes the whole dict or even an element
del example_dict["age"]
print(example_dict)

#clear function is used to empty the dict 
example_dict.clear()
print(example_dict)

del example_dict
print(example_dict)