import json
fp1=open("data.json",'r')
data=json.load(fp1)
print(type(data))
print(data)
fp1.close()