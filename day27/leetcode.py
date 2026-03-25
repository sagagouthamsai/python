"""
bin_n=bin(5)
print(bin_n)
bit_count=0
for i in bin_n:
    if i=="1":
        bit_count+=1
    else:
        continue
print(bit_count)
"""

"""
n=43261596
bin_n=(f"{n:032b}")
print(int(bin_n[::-1],2))


print(int(f"{n:032b}"[::-1],2))
"""
"""
s="   fly me   to   the moon  "
split_s=s.split()
print(split_s)
print(len(split_s[-1]))
"""

s = "0P"
rev_s=s[::-1]
combined_s=""
for i in s.lower():
    if i.isalnum():
        combined_s+=i
print(combined_s[::-1])
print(rev_s)
print(combined_s)