import pymongo

client = pymongo.MongoClient("mongodb+srv://dangduylan:lJCJiSpJuNpzDatG@cluster0-noolz.mongodb.net/test?retryWrites=true")
db = client.bike_rental

def add_bike(model,daily_fee,image,year):
    return db.bikes.insert_one({
        'model':model,
        'daily_fee':daily_fee,
        'image':image,
        'year':year
    })

def get_bike():
    return list(db.bikes.find({}))
    