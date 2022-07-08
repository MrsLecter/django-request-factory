import pymongo
from pymongo import MongoClient
from dateutil import parser
from datetime import datetime


def get_database():
    print('db connected')
    CONNECTION_STRING = "mongodb+srv://guest:guest@cluster0.2vrmo.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    return client['user_shopping_list']

def getAllObject( db="users_basket"):
    dbname = get_database()
    collection_name = dbname[db]
    arr_obj = []
    for x in collection_name.find({}): 
        arr_obj.append(x)
    return arr_obj

def postToDatabase(obj, db="users_basket"):
    dbname = get_database()
    collection_name = dbname[db]
    now = datetime.now()
    create_date = now.strftime("%m/%d/%Y, %H:%M:%S")
    create = parser.parse(create_date)

    collection_name.insert_one(obj)

if __name__ == "main":
    print(getAllObject())