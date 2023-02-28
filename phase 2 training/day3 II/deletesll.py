class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="-->")                  
            temp=temp.next
            
        print("end")
    def insert(self,data):
        new=node(data)
        if self.head is None:
            self.head=new
        elif self.head.data > new.data:
            new.next=self.head
            self.head=new
        else:
            temp=self.head
            while temp.next and new.data:
                temp=temp.next
            new.next=temp.next
            temp.next=new
    def delete(self,key):
        if self.head is None:
            print("list is empty")
        if self.head.data ==key:
            self.head = self.head.next
            return
        temp=self.head
        while temp:
            if temp.data==key:
                break
            prev=temp
            temp=temp.next
        if temp is None:
            print("key not found")
        else:
            prev.next=temp.next
if __name__=="__main__":
    ll=sll()
    print()
    ll.insert(10)
    ll.insert(24)
    ll.insert(56)
    ll.insert(5)

    ll.display()
    ll.delete(5)
    ll.delete(24)
    ll.display()

        
        
            
    
    
        
        
