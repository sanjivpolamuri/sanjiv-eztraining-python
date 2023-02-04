'''a = 10
b = 5

try:
    print(a/b)
except Exception as e:
    print(e)'''


'''while True:
    try:
        n = int(input("Please enter an integer: "))
        if n>0:
            break
    except ValueError:
        print("No valid integer! Please try again ...")
print("Great, you successfully entered an integer than Zero!")'''



'''a = int(input("Enter a Number: "))
if a%2!=0:
        raise Exception("enter the even number")
else:
    print("even")'''
    

# OOPS STRUCTURE

'''all oops is an efficient concept uses in all oops language like java c++ python for multiple reasons we use oops concept for ex. code reusability,data security,hiding data
its a blueprint ex.birds,laptop'''


# object
'''its a thing created based in the class
note:one class have multiple objects
ex.birds
classes laptop : hp,lenovo,dell'''



class laptop():
    a = 10
    b = 20
    print("class variable inside class",a)

    def config(self):
        c = 100
        print("YES")
        print("instance access",self.b)

lenovo = laptop()
print(lenovo)
print(lenovo.a+lenovo.b)
dell = laptop()
print("dell",dell.a)
lenovo.config()
