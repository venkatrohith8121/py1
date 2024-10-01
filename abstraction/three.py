from abc import *
class bank(ABC):
    @abstractmethod
    def cal_tax(self):
        pass
class  account(bank):
    min_bal=500
    def __init__(self,id,name,amount):
        self.acc_id=id
        self.acc_name=name
        self.acc_amount=amount
    def cal_tax(self):
        return self.acc_amount-self.min_bal
a1=account(101,"ROHI",5000)
print(a1.cal_tax())