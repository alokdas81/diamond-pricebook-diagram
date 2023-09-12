from flask import current_app, jsonify, request
import uuid


def get_data():
    with current_app.app_context():
        db = current_app.mongo_client.diamond
        collection = db.basePrice

        args = request.args.to_dict(flat=True)
        data = list(collection.find(args))

    response = jsonify({"data": data})
    return response


def create_data(data):
    with current_app.app_context():
        db = current_app.mongo_client.diamond
        collection = db.basePrice

        for row in data:
            filter_data = row.copy()
            del filter_data["pricePerQuantity"]
            baseprice = list(collection.find(filter_data))
            if len(baseprice) > 0:
                collection.update_one(filter_data, {"$set": row})
            else:
                if "_id" not in row:
                    row["_id"] = str(uuid.uuid4())
                collection.insert_one(row)

    response = jsonify({"message": "Data inserted successfully"})
    return response
