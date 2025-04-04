#method overriding ante parent dantlo unna method name ni malli cjhild lo rasukoni marpulu chesukovadam nachhinattu so avsaram aithe child di call chesthundi feature
class Mobile1990s:
    def m(self):
        ram="thelvad"
        rom="thelvad"
        return "I have nokia super phone"
class Mobile2020(Mobile1990s):
    def m(self):
        ram="mosam"
        rom="mosam"
        return "I have I phone"
class Mobile2020next(Mobile2020):
    def m(self):
       ram="super"
       rom="thop"
       return "I have samsumg Galaxy"
x1=Mobile1990s()
x2=Mobile2020()
x3=Mobile2020next()
#print(x1.m())
print(x2.m())
#print(x3.m())
