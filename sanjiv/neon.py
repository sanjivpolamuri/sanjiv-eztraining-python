l=[]
for i in range(0,5):
    num=int(input())
    l.append(num)
print(l)
for j in l:
    sqr=j*j
    res=sqr%10
    res1=sqr//10
    if res+res1==j:
        print(j,": is neon")
    else:
        print(j,": is not neon")
