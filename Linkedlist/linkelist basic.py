class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist():
    def __init__(self):
        self.head=None
    def print(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
llist=Linkedlist()
llist.head=node(1)
first=node(2)
second=node(3)
llist.head.next=first
first.next=second
llist.print()
