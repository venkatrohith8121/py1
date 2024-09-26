class insuffientbalerror(Exception):
    def __init__(self,msg):
        self.msg=msg
        
def widthdrawl():
    try:
        amount=int(input("enter the withdrawl amount: "))
        acc_bal=5000
        if acc_bal>amount:
            print("withdrawl and enjoy")
        else:
            raise insuffientbalerror("low bal")
    except insuffientbalerror as err:
        print(err.msg)
        
widthdrawl()
print("good Morning")