class Account:
    min_bal=500
    def open_account(self):
        print("account opended succuesfully")
    @classmethod
    def m2(cls):
        pass
    @staticmethod
    def m3():
        pass
a1=Account()
a2=Account()


print(a1.__dict__)
print(a2.__dict__)
print(Account.__dict__)