import pymongo

client=pymongo.MongoClient('mongodb://localhost:27017')
db=client['11am']
user_col=db['user']




client.close()