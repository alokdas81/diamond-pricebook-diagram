from flask import current_app, jsonify, request
import uuid
from app.utils import get_utc_time

def get_data():
    with current_app.app_context():
        db = current_app.mongo_client.diamond
        collection = db.brand

        args = request.args.to_dict(flat=True)
        data = list(collection.find(args))

    response = jsonify({"data": data})
    return response


def create_data(data):
    with current_app.app_context():
        db = current_app.mongo_client.diamond
        collection = db.brand

        for row in data:
            code = row.get("brandCode")
            if code:
                brand_list = list(collection.find({"brandCode": code}))
                if len(brand_list) > 0:
                    row["updatedAt"] = get_utc_time()
                    collection.update_one({"brandCode": code}, {"$set": row})
                else:
                    if "_id" not in row:
                        row["_id"] = str(uuid.uuid4())
                    row["createdAt"] = get_utc_time()
                    row["updatedAt"] = get_utc_time()
                    collection.insert_one(row)

    response = jsonify({"message": "Data inserted successfully"})
    return response
