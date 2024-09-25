class Account:
    def __init__(self,id,name,sal):
        self.eid=id
        self.ename=name
        self.esal=sal


a1=Account(101,'Rahu',50000)
a2=Account(102,'Roja',40000)
a3=Account(103,'ROHI',60000)
print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)