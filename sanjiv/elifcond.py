num=int(input())
if num%2==0 and num>0:
    print("even - positive")
elif num%2==0 and num<0:
    print("evrn - negative")
elif num%2!=0 and num>0:
    print("odd - positive")
elif num%2!=0 and num<0:
    print("odd - negative")
