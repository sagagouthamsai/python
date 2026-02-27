#Count vowels in a string
str="goutham"
vowel_count=0

for i in str:
    if i in "aeiouAEIOU":
        vowel_count+=1
print(vowel_count)