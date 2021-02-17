import pymongo

client = pymongo.MongoClient("mongodb://192.168.99.102:27017/")
db = client["movie"]
films = db["films"]

for f in films.find():
    print(f)

#films.insert_one({"title": "Thor"})
