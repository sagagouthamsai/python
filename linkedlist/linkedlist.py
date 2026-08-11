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
new.show()


