class Employee:
    loc="b101"
e1=Employee()
e2=Employee()
e3=Employee()
print(id(e1))
print(id(e2))#it shows the integer form of the memory location
print(id(e3))
print(e1.__dict__)#turning the obj in the form of dict
print(e2.__dict__)
print(e3.__dict__)
print(Employee.__dict__)#printing the class in the form of dict