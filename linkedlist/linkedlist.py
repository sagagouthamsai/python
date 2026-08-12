class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class linked_list:
    def __init__(self):
        self.head=None

    def insert_at_begining(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode

    def insert_at_end(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=newnode
    
    def del_at_begin(self,data):
        if self.head==None:
            print("List is empty")
            return
        
        self.head=self.head.next

    def show(self):
        temp=self.head
        if temp==None:
            print("\n_______________________________________________________")
            print("list empty")
            print("_______________________________________________________")
            return

        while temp:
            print(temp.data,end="  ")
            temp=temp.next
        print("\n_______________________________________________________")

"""
new=linked_list()
new.show()
new.insert_at_end(1)
new.show()
new.insert_at_end(3)
new.show()
new.insert_at_end(6)
new.show()
new.insert_at_begining(-11)
new.show()
new.insert_at_end(99)
new.show()
new.insert_at_begining(2)
new.show()
new.insert_at_end(1)
new.show()
new.insert_at_begining(0)
new.show()"""


class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class ll:
    def __init__(self):
        self.head=None

    def insert_head(self,data):
        new_node=node(data)

        if self.head:
            self.head.prev=new_node

        new_node.next=self.head
        self.head=new_node


    def insert_tail(self,data):
        new=node(data) 
        if self.head==None:
            self.head=new
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new
        new.prev=temp

    def show_prev_next(self):
        current = self.head

        print("__________________________________________________________________")
        while current:
            prev_value = current.prev.data if current.prev else None
            next_value = current.next.data if current.next else None

            print("Prev:", prev_value,"| Data:", current.data,"| Next:", next_value)
            current = current.next
        print("__________________________________________________________________")

n1=ll()
n1.insert_head(1)
n1.insert_head(9)
n1.insert_head(10)
n1.insert_head(1000)
n1.insert_head(100)
n1.insert_tail(1000)
n1.insert_tail(29)
n1.insert_tail(71)
#n1.show_prev_next()

"""
cur=int(input("Enter the Year you wish to start : "))
n=int(input("Enter how many years you want : "))
res=0
while res<=n:
    if cur%4==0:
        print("Count :",res,"    ","Year :  ",cur)
        res+=1
    cur-=1

    if cur<0:
        print("Hit the limit")
        break"""

"""
n=int(input("Enter the number : "))
bin=""

if not n:
    print(n)

while n:
    bin+=str(n%2)
    n//=2

print(bin[::-1])
print(int("111011101101010111010111",2))"""