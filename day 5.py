'''import random as u
x="srinivas like girls"
print(u.sample(x,1))
a=[1,2,3,4,5,6]
u.shuffle(a)
print(a)
a=[1,2,3,4,5,6]
print(u.choice(a))
b='welcome back'
print(u.choice(b))
s='hello world'
print(u.choices(s,k=3))
print(u.uniform(5,7))'''

'''def digits(n):
    sum = 0
    while n!= 0:
        rem = n % 10
        sum = sum + rem
        n = n//10
    return sum
n = int(input("enter the number:"))
print(digits(123))'''

# recursive function or recursion method a function its called itself

'''def display():
    n = int(input("enter the number:"))
    if n==1:
        display()
    else:
        print("over")

display()'''

# recursion function for factorial of a number

'''def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

print("factorial of 6 is:",fact(int(input())))'''



# fibonacci numbers

'''n = int(input("enter the number:"))
a=0
b=1
sum=0
count=1
while (count<=n):
    print(sum,end=" ")
    count+=1
    a=b
    b=sum
    sum = a+b'''








