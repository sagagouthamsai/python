#set looping is a proccess of accessing every element in the set or specific condition  
example_set={"apple",1,2,3,"zebra",4,"hi"}

#for ele in example_set:
#    print(ele)

for i in example_set:
    if isinstance(i,int) :       
        if i<=3:
            print(i)
        else:
            continue
    if isinstance(i,str):
        if len(i)<=3:
            print(i)
        else:
            continue