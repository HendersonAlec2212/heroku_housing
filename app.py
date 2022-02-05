from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo
import pymongo

#################################################
# Database Setup
#################################################

app = Flask(__name__)

# set up mongo connection

# local
# app.config["MONGO_URI"] = "mongodb://localhost:27017/midland_property_info"

# remote
app.config["MONGO_URI"] = "mongodb+srv://hendersonalec2212:housingvalueheatmap@housing-heatmap-cluster.9teyl.mongodb.net/midland_property_info?retryWrites=true&w=majority"

mongo = PyMongo(app)

# non-flask pymongo
# url = "mongodb+srv://hendersonalec2212:housingvalueheatmap@housing-heatmap-cluster.9teyl.mongodb.net/midland_property_info?retryWrites=true&w=majority"

# mongo = pymongo.MongoClient(url)

#################################################
# Flask Routes
#################################################

@ app.route("/")
def index():
    # homepage
    return render_template("index.html")


@ app.route("/<userInput>")
def load_database(userInput):
    userInput = str(userInput)
    
    # documents = mongo.db.test_properties.find()
    # test_call for just one entry
    documents = mongo.db.properties.find({"address_2":userInput})
    # print(mongo.db.properties)
    print(' ----------------- DOCUMENTS -----------------')
    print(documents)
    print(' ---------------------------------------------')



    
    # set up empty list to hold documents
    query_list = []
    for doc in documents:
        # parse documents taking only what we need at the moment
        marker_dictionary = {}
        marker_dictionary['address_2']= doc['address_2']
        marker_dictionary['owner']= doc['owner']
        marker_dictionary['intensity']=doc['usd_per_building_sqft']
        marker_dictionary['lat'] = doc['lat']
        marker_dictionary['lng']=doc['lng']

        query_list.append(marker_dictionary)
    
    # the return to front-end needs to be a list of dictionaries
    return jsonify(query_list)

    
    # example document in DB
# {
#     "_id": {
#         "$oid": "61e60f8d68822cfcae1f4fb3"
#     },
#     "owner": "PORTER STEPHEN RAY",
#     "address_1": "5401 S COUNTY RD 1140MIDLAND, TX 79706",
#     "address_2": "COUNTY RD 01140 5401 S",
#     "city": "MIDLAND",
#     "state": "TEXAS",
#     "full_address": "COUNTY RD 01140   5401   S MIDLAND, TEXAS",
#     "2021_building_value": 55950,
#     "2021_land_value": 58920,
#     "2021_total_value": 114870,
#     "land_acre": 4.91,
#     "land_sqft": 213880,
#     "est_tax": 1613.89,
#     "total_sqft": 1032,
#     "usd_per_building_sqft": 54.2,
#     "usd_per_total_value_sqft": 111.3,
#     "lat": 32.0031271,
#     "lng": -102.0656771
# }


if __name__ == "__main__":
    app.debug = True
    app.run()
