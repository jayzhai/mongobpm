__author__ = 'Jay Zhai'

import pymongo
from pymongo import MongoClient
import datetime



client = MongoClient('localhost', 27017)

db = client.test_database

collection = db.test_collection

post = {"author": "Mike", "text": "My first blog post!", "tags": ["mongodb", "python", "pymongo"], "date": datetime.datetime.utcnow()}

