# fp1=("one.txt",'r')
# data=fp1.read()
# print(data)
# print("exceted")

fp=None
try:
    fp=open("one.txt",'r')
except:
    fp=open("data.txt",'r')
data=fp.read()
print(data)