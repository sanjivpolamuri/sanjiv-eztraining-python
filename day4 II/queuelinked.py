class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
        self.head= None
        self.last= None
    def enqueue(self,data):
        if self.last is None:
            print("queue is empty")
        else:
            self.last.next=node(data)
            self.last=self.last.next

    def dequeue(self):
        if self.last is None:
            return None
        else:
            to_return=self.head.data
            self.head=self.head.next
            return to_return
    def display():
        print(queue)
a_queue=queue()
while True:
    print("enqueue")
    print("dequeue")
    print("quit")
    print("display")
    do=input("what would you like to do ?").split()
    opr=do[0].strip().lower()
    if opr== "enqueue":
        a_queue.enqueue(int(do[1]))
    elif opr == " dequeue":
        dequeued=a_queue.dequeue()
        if dequeued is None:
            print(" Queue is empty")
        else:
            print(" dequeued elements", int(dequeued))
    elif opr == "quit":
        break
    elif opr=="display":
        a_queue.display()
        break

