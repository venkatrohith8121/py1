import csv
customers=[
    {'id':101,'name':'rahul','avail':True},
    {'id':102,'name':'rohi','avail':False},
    {'id':103,'name':'balu','avail':True}
]
fp1=open("emp.csv",'w',newline="")
wr=csv.writer(fp1)
wr.writerow(['id','name','avail'])
for cust in customers:
    wr.writerow([cust['id'],cust['name'],cust['avail']])
print("new csv file is generated")