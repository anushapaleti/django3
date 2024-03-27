from BasicPrograms.single2 import c
from BasicPrograms.single4 import p1
class p2(c,p1):
    def p3(self):
        print("super parent in p2")


obj2 =p2()
obj2.p3()
obj2.c1()
obj2.parentinfo()