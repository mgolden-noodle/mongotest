#! /usr/bin/python3

import datetime
import pprint  
import pymongo  

from pymongo import MongoClient  

client = MongoClient('mongodb://localhost:27017/')  
db = client.mydb  

#post = { "a" : datetime.datetime.utcnow() }
#db.test.insert(post);
#db.test.insert({ "a" : "hello, world!", "b": "bar"})
#db.test.insert({ "a" : "hello, world!", "b": "baz"})
#db.test.insert({ "a" : "hello, world!"})
#i = 0
#while i<10:
#    db.test.insert({"a": i})
#    i += 1
vv = []
#vv = [{'a': i} for i in range(2)]
vv.append({"a": "believe me!"})
vv.append({"a": "only I can stop it"})
print(vv)
db.test.insert_many(vv, ordered=False)

query = {"a": "hello, world!", "b": {"$exists": False}}
for item in db['test'].find(query):
  pprint.pprint(item)
