#Vowel or Consonant
value=input("Enter an character : ")
match value:
    case x if value.lower() in "aeiou":
        print("vowel")
    case _:
        print("consonant")