# read data.json and create male.json or femlale .json files
import json
fp1=open("data.json",'r')
users=json.load(fp1)
print(type(users))