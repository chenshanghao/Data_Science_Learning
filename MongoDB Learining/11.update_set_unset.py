from pymongo import MongoClient
import pprint

client = MongoClient('mongodb://localhost:27017')
db = client.examples

def find():
    ### update set
    city = db.cities.update({"name": "Munchen",
                             "country": "Germany"},
                             {"$set":{
                             "isoCountryCode": "DEU"
                             }})

    ### update unset
    city = db.cities.update({"name": "Munchen",
                             "country": "Germany"},
                             {"$unset":{
                             "isoCountryCode": ""
                             }})
    ### Don't do this
    db.cities.update({"name": "Munchen",
                      "country": "Germany"},
                      {"isoCountryCode": "DEU"})


if __name__ == '__main__':
    main()