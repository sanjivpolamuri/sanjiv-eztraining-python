q1= """whos rohit sharma favourite person?
a. virat
b. kl rahul
c. Sky
d. Dhoni """
q2= """who is the Pm of india
a. Narendra Modi
b. y.s.jagan
c. Chandra babu
d. KCR"""
q3="""capital of india?
a. Mumbai
b. Delhi
c. Hyderabad
d. Kolkata"""

questions = {q1: "d",q2: "a", q3:"b"} #cc
name = input ("Hi whats ur name   ")
print("Hello", name, "Welcome to the quiz")
score=0
for i in questions:
    print()
    print (i)
    flagl=input ("Do you want to skip thisques (yes)/(no)   ")
    if flagl=="yes":
        continue
    ans = input("enter the answers  ")
    if ans==questions [i]:
        print("Wow! you got one point")
        score=score+1
        print ("your current score is  ",score)
    else:
        print("wrong answer, u lost 1 mark")
        score=score-1

        print ("ur current score is   ", score)
    flag2=input("Do you want to Quit? type (yes/n0)   ")

    if flag2=="yes":
        break
print("your score is :",score)
