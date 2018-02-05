class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist():
    def __init__(self):
        self.head=None
    def push(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node
    def append(self,data):
        new_node=node(data)
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=new_node
    def print(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
llist=Linkedlist()
llist.append(1)
llist.append(2)
llist.push(4)
llist.append(3)
llist.print()
