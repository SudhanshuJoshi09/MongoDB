#!/usr/bin/env python3


import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['newdatabase']

mycol = mydb['newcategory']

person = {"name": "Sudhanshu Joshi", "age": 22}
x = mycol.insert_one(person)

y = mycol.find_one({"name": "Sudhanshu Joshi"})
print(type(y))
print(y)
