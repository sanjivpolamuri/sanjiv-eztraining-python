class node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class Dll:
    def __init__(self):
        self.head=None
    def insertionpos(self,data,pos):
        new=node(data)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        new.prev=temp
        new.next=temp.next
        temp.next.prev=new
        temp.next=new
    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end="<--->")
                temp=temp.next
            print("end")
l=Dll()
n1=node(12)
l.head=n1
n2=node(34)
n3=node(45)
n4=node(67)
n5=node(99)
n2.prev=n1
n1.next=n2
n2.next=n3
n3.prev=n2
n3.next=n4
n4.prev=n3
n4.next=n5
n5.prev=n4
l.insertionpos(500,6)
l.display()
