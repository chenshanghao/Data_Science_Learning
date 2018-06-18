from pymongo import MongoClient
import pprint

client = MongoClient('mongodb://localhost:27017')
db = client.examples

def main():
    city = db.cities.find_one({"name": "Munchen",
                               "country": "Germany"})

    city['isoCountryCode'] = "DEU"
    db.cities.save(city)

if __name__ == '__main__':
    main()