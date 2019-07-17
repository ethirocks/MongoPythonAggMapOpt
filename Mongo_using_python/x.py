from pymongo import MongoClient

def xyz(x,y):
    client = MongoClient()
    db1 = client.mydb
    col = db1.fivek
    col.aggregate([
       { "$match": { "Country": "United Kingdom" } },
       { "$group": { "_id": "$CustomerID", "total": { "$sum": 1} } },
       {"$limit":x},
       {"$skip":y}
    ])

def ten(x,y):
    client = MongoClient()
    db1 = client.mydb
    col = db1.tenk
    col.aggregate([
       { "$match": { "Country": "United Kingdom" } },
       { "$group": { "_id": "$CustomerID", "total": { "$sum": 1} } },
       {"$limit":x},
       {"$skip":y}
    ])
    
def twenty(x,y):
    client = MongoClient()
    db1 = client.mydb
    col = db1.twentyk
    col.aggregate([
       { "$match": { "Country": "United Kingdom" } },
       { "$group": { "_id": "$CustomerID", "total": { "$sum": 1} } },
       {"$limit":x},
       {"$skip":y}
    ])
   
def fifty(x,y):
    client = MongoClient()
    db1 = client.mydb
    col = db1.fiftyk
    col.aggregate([
       { "$match": { "Country": "United Kingdom" } },
       { "$group": { "_id": "$CustomerID", "total": { "$sum": 1} } },
       {"$limit":x},
       {"$skip":y}
    ])