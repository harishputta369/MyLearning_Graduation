#chiled and parent calsses using child extends parent name ani futures inherit aithay
# ploy morphism 2 types
    # 1 operter overloading same operator
    # method over loading
a=10
b=20
class name:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def __add__(self,obj1):
        one=self.fname+obj1.fname
        two=self.lname+obj1.lname
        print(one+","+two)



x=name("Harish","putta")
#x.Add()
y=name("shiv","Pw")
x+y
#print(y.lname)