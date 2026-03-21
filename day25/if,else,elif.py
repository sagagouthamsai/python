#if, elif, and else are used for decision making,they execute a block of code if the condition is true

#if 
"""
The if statement checks a condition.
If the condition is True, the code inside runs
"""

age = 16

if age >= 18:
    print("major")

#if-else:
#Used when you want two possible outcomes.
#else runs when if condition is False

if age >= 18:
    print("major")
else:
    print("minor")

#elif:
#Used when you have multiple conditions.
#Conditions are checked top to bottom
#Only the first true condition runs

if age >= 18:
    print("major")
elif age<=0:
    print("no negative numbers")
else:
    print("minor")

