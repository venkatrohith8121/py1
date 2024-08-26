l1=[10,20,30,40,10,30,"rahul"]
print(l1)
# adding an element at the last of the list
l1.append('rohi')
print(l1)
# insert-> adding the element at the desired index position nad the elements in the list will be moved a bit right side
# if index in not available also it will be added to the list
l1.insert(1,2323)
print(l1)
# replacing the element with new element
# if index in not present here it shows the index error 
l1[1]="king"
print(l1)
# extend -> it extends the list with another list
l2=[2225,'nithin']
l1.extend(l2)
print(l1)