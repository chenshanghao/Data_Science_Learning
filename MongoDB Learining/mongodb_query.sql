# exist
db.cities.find({"governmentType": {"$exists": 1}}).count()

# regex operator
db.cities.find({"motto": {"$regex": "[Ff]riendship"}}).pretty()

# query using scalars
db.autos.find({"modelYears": 1980}).pretty()

# Using $in operator (contain any of the value)
db.autos.find({"modelYears": {"$in": [1965, 1966, 1967]}}).count()

# Using $all operator (contain all of the value)
db.autos.find({"modelYears": {"$all": [1965, 1966, 1967]}}).count()

# Do not notation
db.autos.find({"dimensions.weight": {"$gt": 5000}})

# remove not has city name
db.cities.find({"name": {"$exosts": 0}})

# remove entire collection
db.cities.drop()