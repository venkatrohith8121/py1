emp={
    'id':101,
    'ename':'rahul gandhi'
}
# /if the id provided here is the already there in the dict then no changes will be done
# if it is not there then create the new property
x=emp.setdefault('extra_id','102')
print(x)
print(emp)
