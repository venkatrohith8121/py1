# LIST DATA STRUCTURE READ OPERATION METHOD
enames=['rohi','modi','sonia','sonia','sonia']
enames.sort()# ascending order
print(enames)

enames.sort(reverse=True)#descending order sorting
print(enames)

x=enames.index('sonia') #it shows the index value of the desired element
print(x)

y=enames.count('sonia')# it counts no.of occurences in the list
print(y)

