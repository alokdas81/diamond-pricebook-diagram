from flask import current_app, jsonify, request
import uuid
from app.utils import get_utc_time

def get_data():
    with current_app.app_context():
        db = current_app.mongo_client.diamond
        collection = db.series
        args = request.args.to_dict(flat=True)
        data = list(collection.find(args))

    response = jsonify({"data": data})
    return response


def create_data(data):
    with current_app.app_context():
        db = current_app.mongo_client.diamond
        collection = db.series

        for row in data:
            code = row.get("seriesCode")
            if code:
                series_list = list(collection.find({"seriesCode": code}))
                if len(series_list) > 0:
                    row["createdAt"] = get_utc_time()
                    row["updatedAt"] = get_utc_time()
                    collection.update_one({"seriesCode": code}, {"$set": row})
                else:
                    if "_id" not in row:
                        row["_id"] = str(uuid.uuid4())
                    row["createdAt"] = get_utc_time()
                    row["updatedAt"] = get_utc_time()
                    obj = collection.insert_one(row)

    response = jsonify({"message": "Data inserted successfully"})
    return response
