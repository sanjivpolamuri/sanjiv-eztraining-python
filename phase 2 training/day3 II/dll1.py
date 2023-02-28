class node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class Dll:
    def __init__(self):
        self.head=None
    def insertion(self):
        new=node(100)
        temp=self.head
        temp.prev=new
        new.next=temp
        self.head=new
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
n2.prev=n1
n1.next=n2
n2.next=n3
l.insertion()
l.display()
