from pymongo import MongoClient
import pprint

client = MongoClient('mongodb://localhost:27017')
db = client.examples

def find():
    ### update set  multi update
    city = db.cities.update({"name": "Munchen",
                             "country": "Germany"},
                             {"$set":{
                             "isoCountryCode": "DEU"
                             }}, multi = True)


if __name__ == '__main__':
    main()