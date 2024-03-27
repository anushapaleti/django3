class base1():
    def baseinfo(self):
        print("Inside Base1")
class p1(base1):
    def parentinfo(self):
        print("Inside p1")
obj1 = p1()
obj1.parentinfo()
obj1.baseinfo()