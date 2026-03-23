
#Even or Odd
value_=int(input("enter an number : "))
match value_:
    case x if x%2==0:
        print("even")
    case x if x%2!=0:
        print("odd")

