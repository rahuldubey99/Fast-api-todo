from pymongo import MongoClient

MONGO_URI = "mongodb+srv://rahul:Rahuldubey123@cluster0.uha5oea.mongodb.net/"

client = MongoClient(MONGO_URI)
db = client.get_database("Learn")
conn = db.get_collection("fastApi")  
