class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class ll:
    def __init__(self):
        self.head=None

    def insert_at_begin(self,data):
        new=node(data)
        new.next=self.head
        self.head=new

    def insert_at_end(self,data):
        new=node(data)
        if not self.head:
            self.head=new
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new

    def del_at_begin(self):
        if not self.head:
            print("list is empty")
            return
        self.head=self.head.next

    def del_at_end(self):
        if not self.head:
            print("list is empty")
            return

        if not self.head.next:
            self.head=None

        temp=self.head

        while temp.next.next:
            temp=temp.next
        temp.next=None

    def display(self):
        print("___________________________________________________________")
        if not self.head:
            print("list is empty")
            return
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next


n=ll()
n.display()
n.insert_at_begin(1)
n.insert_at_begin(100)
n.insert_at_begin(29)
n.display()
n.insert_at_end(67)
n.display()
n.del_at_begin()
n.display()
n.del_at_end()
n.display()


class dn:
    def __init__(self,data):
        self.data=data
        
        self.next=None
        self.prev=None
