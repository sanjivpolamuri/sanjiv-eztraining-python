class overload:
    def display(self,a=None,b=None):
        print(a,b)
obj=overload()
obj.display()
print("without arg")

obj.display(10,22)
print("with arg")

obj.display(66)
print("with onw arg")
