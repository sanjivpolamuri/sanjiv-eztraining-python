queue=[]

def enqueue():
    ele=int(input("enter the elements:"))
    queue.append(ele)
    print(queue)
def dequeue():
    if not queue:
        print("queue is empty")
    else:
        e=queue.pop(0)
        print("removed element",e)
        print(queue)
def display():
    print(queue)


while True:
    print("select operations 1.enqueue 2.dequeue 3.display 4.quit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("The End")
    
