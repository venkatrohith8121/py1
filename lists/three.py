marks=[35,36,37,38,39,40]
total=0
for mark in marks:
    total=total+mark

print("total marks:",total)

print("**************************")
i=0
total=0
while i<=len(marks)-1:
    total=total+marks[i]
    i+=1
print("total marks:",total)