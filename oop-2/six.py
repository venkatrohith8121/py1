class test:
    def __init__(self):
        self.a=100
    def m1(self):
        self.b=200
        @classmethod
    def m2(cls):
        self.d=400
t1=test()
t2=test()
t1.m1()
t2.c=300
print(t1.__dict__)
print(t2.__dict__)