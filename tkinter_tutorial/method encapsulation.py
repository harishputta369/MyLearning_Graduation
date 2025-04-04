class X:
    def a(self):
        return "public"
    def _b(self):
        return "private"
    def __c(self):
        return "Strictly private or protected"
y=X()
print(y.a())
print(y._b())
#print(y._X__c())