import json
fp1=open("user.json",'r')
users_list=json.load(fp1)
employes=[]

for user in users_list:
    employes.append({'eid':user['id']})
fp2=open("employes.json",'w')
json.dump(employes,fp2)

fp1.close()
fp2.close()