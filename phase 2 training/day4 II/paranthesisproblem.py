s=input()
stack=[]
check=True
for char in s:
    if(char== "(" or char== "{" or char=="["):
        stack.append(char)
    elif char=="]":
        if(len(stack) and stack.pop()!="["):
            check=False
            break
    elif char=="}":
        if(len(stack) and stack.pop()!="{"):
            check=False
            break
    elif char==")":
        if(len(stack) and stack.pop()!="("):
            check=False
            break
    else:
        check=False
        break

if(check==False or len(stack)):
    print("not matched")
else:
    print("matched")
