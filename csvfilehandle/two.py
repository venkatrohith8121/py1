import csv
fp=open("emp.csv",'r')
rows=csv.reader(fp)
users=list(rows)
print(users)
for user in users[1:]:
    print(user)