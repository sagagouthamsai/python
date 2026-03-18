#1. Count frequency of elements
"""class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        dict_value={}
        for ele in arr:
            if ele in dict_value:
                dict_value[ele]+=1
            else:
                dict_value[ele]=1
        if len(dict_value.values())==len(set(dict_value.values())):
            return True
        else:
            return False
        

sol = Solution()
result = sol.uniqueOccurrences(arr=[1, 2, 2, 1, 1, 3])"""

#Find Key with Maximum Value
d = {"a":10, "b":25, "c":15}
max_value=max(d.values())
for key,value in d.items():
    if value==max_value:
        print(key)
    else:
        continue

#Merge Two Dictionarie
d1 = {"a":1}
d2 = {"a":2, "b":3}
d3 = {"b":4, "c":5}

result=d1.copy()

for i,j in d2.items():
    if i in result:
        result[i]+=j
    else:
        result[i]=j
for i,j in d3.items():
    if i in result:
        result[i]+=j
    else:
        result[i]=j

print(result)

#Count Characters in String
s="sai sai"
string_value=s.split()
list_str=[]
dict_string={}
for str in string_value:
    for char in str:
        list_str+=char

for ele in list_str:
    if ele in dict_string:
        dict_string[ele]+=1
    else:
        dict_string[ele]=1
print(dict_string)


#optimized gpt version usecase 1
s="sai sai"
dictnry_value={}
for strngs in s:
    if strngs!=" ":
        dictnry_value[strngs]=dictnry_value.get(strngs,0)+1

print(dictnry_value)

