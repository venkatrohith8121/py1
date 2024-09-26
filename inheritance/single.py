class parent:
    def m1(self):
        print("m1-method")
    def m2(self):
        print("m2-method")
class child(parent):
    def m3(self):
        print("m3-method")
obj=child()
obj.m1()
obj.m2()
obj.m3()