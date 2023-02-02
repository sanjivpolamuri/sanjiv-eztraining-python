num = int(input("enter the number:"))
if (num%2==0) and (num>=0):
    print("Even-Positive")
elif (num%2!=0) and (num>=0):
    print("Odd-Positive")
elif (num%2==0) and (num<0):
    print("Even-Negative")
else:
    print("Odd-Negative")
