#! /usr/bin/python3

import datetime
import pprint  
import pymongo  

from pymongo import MongoClient  

client = MongoClient('mongodb://localhost:27017/')  
db = client.mydb  

post = { "a" : datetime.datetime.utcnow() }
postId = db.test.insert(post);  
postId2 = db.test.insert({ "a" : "hello, world!"})
i = 0
while i<10:
    db.test.insert({"a": i})
    i += 1

query = {"a": "hello, world!"}
for item in db.test.find(query):
  pprint.pprint(item)
