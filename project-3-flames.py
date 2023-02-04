name1=input("Enter the namel:").lower()
name2=input("Enter the name2:").lower() 
namel=namel.replace(" ","")
name2=name2.replace(" ","")
print(name1)
print(name2)
for i in name1:
    for j in name2:
        if i==j:
            namel=namel.replace (i,"",1)
            name2=name2.replace (j,1)
            break
count=len(name1+name2)
print(count)
if count>0:
    count=len (name1+name2)
print (count)
if count>0:
    list1=["Friends", "Lovers", "Affectionate", "Marriage","Enemy","Sister"]
    while len(list1)>1:
        c=count%len(list1)
        s_index=c-1


        if s_index>=0: 
            left=list1[:s_index]
            right=list1[s_index+1:]
            list1=right+left
        else:
            list1=list1[:len (list1) -1]
    print("Relationship :",listl[0])
else:
    print ("Enter different names")
