class Account():
    "hi i am ROhi"
    min_bal=500
    def __init__(self,id,name,amount):
        self.acc_id=id
        self.acc_name=name
        self.acc_bal=amount
    def deposit_amount(self,amount):
        self.acc_bal=self.acc_bal+amount



# print(Account.__dict__)
print(Account.__doc__)























# a1=Account(101,'Rahul',45000)
# a1.deposit_amount(2500)
# a1.deposit_amount(3000)
# a2=Account(102,'Ranjith',55000)
# a3=Account(103,'Rohi',80000)
# a3.deposit_amount(50000)


# print(a1.__dict__)
# print(a2.__dict__)
# print(a3.__dict__)