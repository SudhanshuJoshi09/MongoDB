#!/usr/bin/env python3


import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017')
mydb = myclient['somedatabase']

mycol = mydb['newcollection']

dict = {"email": "random@random.com", "password": "Something"}

x = mycol.insert_one(dict)

z = mycol.find(dict)
print(z)

# For deleting record.
mycol.delete_one(dict)
