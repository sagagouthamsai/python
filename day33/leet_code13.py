s = "MCMXCIV"
values = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }
integer=0
for i in range(len(s)):
    if i+1<len(s) and values[s[i+1]]>values[s[i]]:
        integer-=values[s[i]]
        print(integer)
    else:
        integer+=values[s[i]]
        print(integer)

print(integer)