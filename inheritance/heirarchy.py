class parent:
    def m1(Self):
        print("m1-method")
class child1(parent):
    def m2(Self):
        print("m2-method")
class child2(parent):
    def m3(Self):
        print("m3-method")
obj1=child1()
obj2=child2()
obj1.m1()
obj1.m2()
obj2.m1()
obj2.m3()