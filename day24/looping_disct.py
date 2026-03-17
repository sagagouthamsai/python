#to print all the key values we use loops
example_dict={'type' : 'fruit', 'name' : 'apple','color':'red'}

print('method-1 key value')
for key_value in example_dict:
    print(key_value)

print('method-2 key value')
for key_value in example_dict.keys():
    print(key_value)


#we can also use loops to print or return all values also

print('method-1 value')
for values in example_dict:
    print(example_dict[values])

print('method-2 value')
for values in example_dict.values():
    print(values)



