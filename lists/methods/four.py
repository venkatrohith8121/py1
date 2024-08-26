l1=[4,5,6,7,8]
l2=l1.copy()# in this prcess we r cloning the list obj
print(l2)

l3=l2# it is giving the alias name to same list obj
print(l3)

print(id(l1))
print(id(l2))#it has diff id belongs to the l1
print(id(l3))#l2 and l3 having the same id since it is assing the alias name for the same list obj
