class Account():
    def __init__(self,id,name,amount):
        self.acc_id=id
        self.acc_name=name
        self.acc_amount=amount
        
a1=Account(101,'Rahul',45000)
a2=Account(102,'Ranjith',55000)
a3=Account(103,'Rohi',75000)



print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)