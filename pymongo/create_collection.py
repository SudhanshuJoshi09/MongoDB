#!/usr/bin/env python3


import pymongo

# Setting up the database.
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']

# Creating collection.
mycol = mydb['students']
print(mydb.list_collection_names())
