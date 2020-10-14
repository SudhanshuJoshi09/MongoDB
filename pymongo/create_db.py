#!/usr/bin/env python3

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

# In mongo the database is only created when there is something added to it.
