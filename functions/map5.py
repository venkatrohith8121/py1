numbers=[1,1,1,1,1]
def addplus(number):
    return number+1
map_obj=map(addplus,numbers)
# l=list(map_obj)
# t=tuple(map_obj)
s=set(map_obj)
# print(l)
print(s)
# print(t)