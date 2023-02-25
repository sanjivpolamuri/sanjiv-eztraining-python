class node:
    def __init__(self,data):
        self.data=data
        self.next= None
class sll:
    def __init__(self):
        self.head= None
    def display(self):
        if self.head is None:
            print("sll is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
obj=sll()
n=node("W")
obj.head=n
n1=node("I")
obj.head.next=n1
n2=node("N")
n1.next=n2
n3=node("N")
n2.next=n3
n4=node("E")
n3.next=n4
n5=node("R")
n4.next=n5
n5.next=None
obj.display()
