# import csv
import json
customers=[
    {'id':101,'name':'rahul','avail':True},
    {'id':102,'name':'rohi','avail':False},
    {'id':103,'name':'balu','avail':True}
]
fp1=open("emp.json",'w')
# fp2=open("emp.csv",'w')
json.dump(customers,fp1)
print("new json file is created")
fp1.close()

