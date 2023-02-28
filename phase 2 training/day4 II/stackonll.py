class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.head=None
    def isempty(self):
        if self.head==None:
            self.head=new
    def push(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            new=node(data)
            new.next=self.head
            self.head=new
    def pop(self):
        if self.isempty():
            return None
        else:
            pnode=self.head
            self.head=self.head.next
            pnode.next=None
            return pnode.data
    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data
    def display(self):
        t=self.head
        if self.isempty():
            print("stack underflow")
        else:
            while(t!=None):
                print(t.data,end=" ")
                t=t.next
                if(t!= None):
                    print("-->", end=" ")
            return
if __name__=="__main__":
    s=stack()
    s.push(11)
    s.push(12)
    s.push(13)
    s.push(14)
    s.push(15)
    s.display()
    print()
    print(s.peek())
    s.pop()
    s.peek()
    s.display()
