import datetime
import pprint  
import pymongo  

from pymongo import MongoClient  

client = MongoClient('mongodb://localhost:27017/')  
db = client.mydb  

post = { "a" : datetime.datetime.utcnow() }  
postId = db.test.insert(post);  
postId2 = db.test.insert({ "a" : "hello, world!"})

find = db.test.find()  
for item in db.test.find() :   
  pprint.pprint(item)  
