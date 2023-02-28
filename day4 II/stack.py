stack=[]

def push():
    ele=int(input("enter the element:"))
    stack.append(ele)
    print(stack)
def pop():
    if not stack:
        print("stack is empty:")
    else:
        e=stack.pop()
        print("removed element:",e)
        print(stack)
def display():
    while stack:
        print(stack)
        break
while True:
    print("select operations 1. push 2.pop 3.display 4.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("The End")
