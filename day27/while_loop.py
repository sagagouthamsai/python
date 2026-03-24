#while loop is a type of loop that loops around a statment until the condition is meet 
#this  loop continues endlessly until the break condition is meet

#syntax 
#while condition:
#   statement

i = 1

while i <= 5:
    print(i)
    i += 1

#User Input Loop
num = 0
while num != -1:
    num = int(input("Enter number (-1 to stop): "))

#break: break is used to stop looping
i = 1

while True:
    if i == 5:
        break
    print(i)
    i += 1

#continue:continue is used to skip a part of loop
i = 0

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
