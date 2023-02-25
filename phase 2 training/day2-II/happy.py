def happy(n):
    r=s=0
    while(n>=0):
        for i in range(0,len(str(n))+1):
            r=n%10
            s+=r**2
            n=n//10
        return s


n=int(input())
res=n
while res!=1 and res!=4:
    res=happy(res)
if res==1:
    print("Happy Number")
else:
    print("Sad Number")
