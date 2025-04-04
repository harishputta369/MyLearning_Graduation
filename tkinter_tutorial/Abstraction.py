#abstraction ante just declare chestham but instatiate cheyam ante class create cheyam
#em chesina child classes thine cheyali so child classes create cheyochhu ani ardtham
from abc import ABC,abstractclassmethod#
class parent(ABC):#
    @abstractclassmethod
    def somthing(self):
        pass
    def p(self):
        return "I'm parent"
class child(parent):#
    def smt(self):
        return "i'm child"
class schild(child):#
    def sm(self):
        return "i'm super child"
    def somthing(self):
        return "haha i'm super child"
#x=child()
#print(x.smt())
#print(x.somthing())
y=schild()
print(y.p())
print(y.smt())
print(y.sm())
print(y.somthing())

