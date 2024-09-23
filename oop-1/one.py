class employee:
    pass
e1=employee()
e2=employee()
e3=employee()
print(id(e1))
print(id(e2))#it shows the integer form of the memory location
print(id(e3))
print(e1.__dict__)
print(e2.__dict__)
print(e3.__dict__)