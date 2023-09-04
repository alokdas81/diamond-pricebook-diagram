from flask import Flask, request, jsonify
import urllib 
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB configuration
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/diamond'
app.config['MONGO_URI'] = 'mongodb+srv://'+  urllib.parse.quote("ogma") +':'+ urllib.parse.quote("ogma123")+'@pricebookcluster.fpwwf4a.mongodb.net/?retryWrites=true&w=majority'
mongo = MongoClient(app.config['MONGO_URI'])

db = mongo.diamond


@app.route('/insert_manufacturer', methods=['POST'])
def insert_manufacturer():
    data = request.json
    manufactur_list = []
    for row in data:
        manufactur_dict = { 
            "code": row['code'], 
            "description": row['description'], 
            "contact": row['contact'] 
            }
        manufactur_list.append(manufactur_dict)
    
    db.manufacturer.insert_many(manufactur_list)

    return jsonify({'message': 'Data inserted successfully'})


@app.route('/get_manufacturer', methods=['GET'])
def get_manufacturer():

    data = list(db.manufacturer.find({}, {'_id': 0}))

    return jsonify(data)


@app.route('/insert_brand', methods=['POST'])
def insert_brand():
    data = request.json
    brand_list = []
    for row in data:
        brand_dict = {
            "code": row['code'], 
            "description": row['description'], 
            "contact": row['contact'], 
            "manufacturer": row['manufacturer']
            }
        brand_list.append(brand_dict)
    db.brand.insert_many(brand_list)
    
    return jsonify({'message': 'Data inserted successfully'})


@app.route('/get_brand', methods=['GET'])
def get_brand():
    manufacturer = request.args.get('manufacturer')
    query = {}

    if manufacturer:
        query['manufacturer'] = manufacturer

    data = list(db.brand.find(query, {'_id': 0}))

    return jsonify(data)


@app.route('/insert_series', methods=['POST'])
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

    return jsonify(data)


@app.route('/get_features', methods=['GET'])
def get_features():
    series = request.args.get('series')
    if not series:
        return jsonify({"error": "series is required"}), 400
    query = {}
    if series:
        query['code'] = series

    data = list(db.series.find(query, {'_id': 0}))
    response = []
    for row in data:
        features = row.get('features', [])
        adonFeatures = row.get('adonFeatures', [])
        features_dict = {}
        if features:
            features_data = db.features.find({'UID': {'$in': features}}, {'_id' : 0})
            features_dict["features"] = list(features_data)
        if adonFeatures:
            adonFeatures_data = db.adonFeatures.find({'UID': {'$in': adonFeatures}}, {'_id' : 0})
            features_dict["adonFeatures"] = list(adonFeatures_data)

        response.append(features_dict)

    return jsonify(response)


@app.route('/get_baseprice', methods=['POST'])
def get_baseprice():
    data = request.json
    baseprice = db.basePrice.find(data, {'_id' : 0})
    return jsonify(list(baseprice))

if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')