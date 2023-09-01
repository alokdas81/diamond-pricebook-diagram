from flask import Flask, request, jsonify
import urllib 
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB configuration
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/diamond'
app.config['MONGO_URI'] = 'mongodb+srv://'+  urllib.parse.quote("ogma") +':'+ urllib.parse.quote("ogma123")+'@pricebookcluster.fpwwf4a.mongodb.net/?retryWrites=true&w=majority'
mongo = MongoClient(app.config['MONGO_URI'])

db = mongo.diamond


@app.route('/insert', methods=['POST'])
def insert_data():
    data = request.json

    collections_to_insert = {
        "series": db.series,
        "features": db.features,
        "basePrice": db.basePrice,
        "adonFeatures": db.adonFeatures
    }

    for collection_name, collection in collections_to_insert.items():
        data_to_insert = data.get(collection_name)
        if data_to_insert:
            collection.insert_many(data_to_insert)

    return jsonify({'message': 'Data inserted successfully'})


'''
Endpoint be link: http://localhost:5001/get_series?manufacturer=Allegion&brand=LCN
'''
@app.route('/get_series', methods=['GET'])
def get_series():
    manufacturer = request.args.get('manufacturer')
    brand = request.args.get('brand')

    query = {}

    if manufacturer:
        query['manufacturer'] = manufacturer

    if brand:
        query['brand'] = brand

    data = list(db.series.find(query, {'_id': 0}))

    # Check if any data is found
    if len(data) == 0:
        return jsonify({'message': 'No data found for the given query.'}), 404

    return jsonify(data)


@app.route('/get_features', methods=['POST'])
def get_features():
    data = request.json
    response = {}
    if "features" in data:
        features = db.features.find({'UID': {'$in': data['features']}}, {'_id' : 0})
        response["features"] = list(features)
    if "adonFeatures" in data:
        adonFeatures = db.adonFeatures.find({'UID': {'$in': data['adonFeatures']}}, {'_id' : 0})
        response["adonFeatures"] = list(adonFeatures)
    # if "filteredFeatures" in data:
    #     filteredFeatures = db.features.find({'UID': {'$in': data['features']},"$or": [{'availabilityCriteria': {"$exists": True,"$size": 0}},{'availabilityCriteria': data['filteredFeatures']}]}, {'_id' : 0})
    #     response["features"] = list(filteredFeatures)
    # if "filteredAdonFeatures" in data:
    #     filteredAdonFeatures = db.adonFeatures.find({'UID': {'$in': data['adonFeatures']},"$or": [{'availabilityCriteria': {"$exists": True,"$size": 0}},{'availabilityCriteria': data['filteredAdonFeatures']}]}, {'_id' : 0})
    #     response["adonFeatures"] = list(filteredAdonFeatures)
    return jsonify(response)


@app.route('/get_baseprice', methods=['POST'])
def get_baseprice():
    data = request.json
    baseprice = db.basePrice.find(data, {'_id' : 0})
    return jsonify(list(baseprice))

if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')