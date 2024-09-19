import csv
fp=open("emp.csv",'r')
rows=csv.reader(fp)
for row in rows:
    print(row[0])
    print(row[1])
    print(row[2])