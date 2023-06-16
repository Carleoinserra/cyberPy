import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]


appcoll = mydb["blogcollection"]
document = {"user_id": 1, "user": "test"}
appcoll.insert_one(document)

print(myclient.list_database_names())

dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")
else:
   print ("non esiste")