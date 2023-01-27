import pymongo
from pymongo import MongoClient
from Listfile import CommonList

if __name__ == "__main__":
    print("Welcome to pymongo")
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    print("Connection Successful")
    db = client['pythonApp']
    collections = db['loginData']
    # dictionary = {'name': 'ankita', 'age': '21', 'company': 'cars24'}
    # collections.insert_one(dictionary)
    for item in CommonList.reqData:
        print(item)
        for it in item:
            insertThese = [
                {'Name': item["name"]}, {'code': item["code"]}]




    collections.insert_many(insertThese)
