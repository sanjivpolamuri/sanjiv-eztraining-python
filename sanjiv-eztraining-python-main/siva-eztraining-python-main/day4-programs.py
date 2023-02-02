#create a neww dict
'''d={n:n for n in range(1,6))
print(d)'''


#calculate total bill
'''d = {"rice":60 , "dhaal":150 , "oil":199}
sum=0
new={product:price*5 for (product,price) in old.items()}
for i in new.values():
    sum+=i
print(new)
print(sum,"total bill")
'''



#create list with 8 customer names display a dict which has customers names along with discounts for them from a particular shop
'''
import random
cust=["shinchan","bochan","siva","sanjiv","mythri","sri","shobha","rambabu"]
cust_dict={names: random.randint(1,100) for names in cust}
print(cust_dict)
'''


'''
stu=["shinchan","bochan","kingjong","shin","chan"]
stu_marks=[250,500,475,300,400]
dict={a:(b/500)*100 for (a,b) in zip(stu,stu_marks)}
print(dict)

'''


#s="hi veeraya"
      
'''s="hi veerendra"
print(s)
print( s.upper())
print (s.lower())
print (s.capitalize())
print (s.replace("veeraya","venkayya"))
print (s.strip())
print (s.split(","))
print (s.center(50,'$'))
print (s.count("a"))
print (s.index("v"))
print (s.find("y"))
print (s.startswith('hi'))
print (s.endswith('a'))'''

# create a string and tell given character is in string 


'''st = input()
st = st.replace(" ","")
ch = input()
for i in st:
    if i==ch:
        print("yes ch is in string")'''


# Given string is palendrome or not
'''st = input()
rs = st[::-1]
print(rs)
if st==rs:
    print("yes")'''



# check ur string contains space or not if yes count number of spaces.

'''rt = input()
count = 0
for i in rt:
    if i==" ":
        count+=1
if count>0:
    print("yes")
    print(count)
else:
    print("No")'''

# create a list with vowels take input from user count vovwels from the string and display the vowels

lst = list(map(str,input("enter the strings:").split()))
print(lst)
vow = ['a','e','i','o','u','A','E','I','O','U']
vowels=[]
for i in lst:
    for j in i:
        if j in vow:
            vowels.append(j)
print(list(set(vowels)))

