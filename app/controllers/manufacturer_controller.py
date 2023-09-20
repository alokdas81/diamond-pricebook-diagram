from flask import current_app, jsonify
import uuid
from app.utils import get_utc_time

def get_data():
    with current_app.app_context():
        db = current_app.mongo_client.diamond
        collection = db.manufacturer
        data = list(collection.find({}))

    response = jsonify({"data": data})
    return response


def create_data(data):
    with current_app.app_context():
        db = current_app.mongo_client.diamond
        collection = db.manufacturer

        for row in data:
            code = row.get("manufacturerCode")

            if code:
                manufacturer_list = list(collection.find({"manufacturerCode": code}))
                if len(manufacturer_list) > 0:
                    row["updatedAt"] = get_utc_time()
                    collection.update_one({"manufacturerCode": code}, {"$set": row})
                else:
                    if "_id" not in row:
                        row["_id"] = str(uuid.uuid4())
                    row["createdAt"] = get_utc_time()
                    row["updatedAt"] = get_utc_time()
                    insert_id = collection.insert_one(row)
                    # print(insert_id.inserted_id)

    response = jsonify({"message": "Data inserted successfully"})
    return response
