list_value=[1,2,3,4,5]

def list_sum(l_val):
    if not isinstance(l_val,list):
        return "Please enter a valid list"
    return sum(list_value)

a=list_sum((1,2,3,4,5))
print(a)

print(list_sum([1,2,3,4,5]))

