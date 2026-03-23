#match is an advanced form of switch in python
#this is used to reduce execive use if if statements
#syntax
value = 2
match value:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Default case")

#default case 
#for default case we use case _

#match multiple values in one case
num = 4
match num:
    case 1 | 2 | 3:
        print("Small number")
    case 4 | 5 | 6:
        print("Medium number")





