#accessing dictionaries 
#we can access dictionaries with the help of key value index
#we use dict_name[key_value]
example_dict={"name":"goutham","age":19,"clg":"jbiet","institute":"jbiet"}
print(example_dict["name"])

#key()
#we can use this function to get all the key_values in the dictionary
#syntax dict_name.keys()
key_values=example_dict.keys()
print(key_values)

#values()
#this returns all the values in dict
#syntax dict_name.values()
value_values=example_dict.values()
print(value_values)

#items()
#this function returns key value pairs in the form of tuple,list
print(example_dict.items())

#checking
if "name" in example_dict:
    print("yes")



