import json
import requests
import csv
api_url='https://jsonplaceholder.typicode.com/users'
user_data=None
try:
    user_data=requests.get(api_url)
    
except:
    fp=open("user.json",'r')
    user_data=json.load(fp)
users=user_data.json()
print(type(users))