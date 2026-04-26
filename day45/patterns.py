n=5
for i in range(n+1,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

for i in range(n+1):
    for j in range(i):
        print("*",end=" ")
    print()

print("\n")

for i in range(n+1):
    for j in range(n+1):
        print("*",end=' ')
    print("")

for i in range(n+1):
    star="*"*(2*i-1)
    print(star.center(2*n))
    

    