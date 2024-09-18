# read data.json and create male.json or femlale .json files
import json
fp1=open("data.json",'r')
users=json.load(fp1)
male_users=list(filter(lambda user:user['gender']=="Male",users))
female_users=list(filter(lambda user:user['gender']=="Female",users))

fp2=open("male.json",'w')
fp3=open("female.json",'w')
json.dump(male_users,fp2)
json.dump(female_users,fp3)