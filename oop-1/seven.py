class Amount:
    acc_bal=0
    def deposit_amount(self,amount):
        self.acc_bal=self.acc_bal+amount
        
a1=Amount()
a2=Amount()
a1.deposit_amount(5000)
a2.deposit_amount(2000)
print(a1.__dict__)
print(a2.__dict__)