numbers=[10,20,30,40]
def addplus(num):
    return num+1
mapobj=map(addplus,numbers)
new=list(mapobj)
print(numbers)
print(new)