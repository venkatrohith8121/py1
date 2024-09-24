class test:
    def __init__(self):
        print("tst")
    def m1(self):
        print("tst instance")
    @classmethod
    def m2(self):
        print("tst class")
    @staticmethod
    def m3(self):
        print("tst static")
t1=test()
t2=test()
t1.m1()