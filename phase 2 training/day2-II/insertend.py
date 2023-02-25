class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insertionend(self,data):
        new=node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new
            
    def display(self):
        if self.head is None:
            print("sll is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
        
obj=sll()
n=node(10)
obj.head=n
n1=node(29)
obj.head.next=n1
n2=node(89)
n1.next=n2
n3=node(66)
n2.next=n3
n4=node(78)
n3.next=n4
n5=node(143)
n4.next=n5
n5.next=None
obj.insertionend(33)
obj.display()
