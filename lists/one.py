l1=[10,20,30,40,50,60]
print(l1)
print(type(l1))

eids=[101,102,103,104,105]
# indexing starts from  0 to n-1
print(eids)
print(eids[0])
print(eids[1])
print(eids[2])
print(eids[3])
print(eids[4])
# -ve indexing is also possible

print(eids[-1])

# index not available Error
print(eids[41])
#  File "E:\pro stack\py 1\lists\one.py", line 18, in <module>
#     print(eids[41])
#           ~~~~^^^^
# IndexError: list index out of range