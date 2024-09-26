class gp:
    def m1(self):
        print("m1-method")
class p1(gp):
    def m2(self):
        print("m2-method")
class p2(gp):
    def m3(self):
        print("m3-method")
class child(p1,p2):
    def m4(self):
        print("m4-method")
obj=child()
obj.m1()
obj.m2()
obj.m3()
obj.m4()