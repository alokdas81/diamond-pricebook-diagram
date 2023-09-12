from flask import current_app, jsonify, request
import uuid


def get_data():
    with current_app.app_context():
        db = current_app.mongo_client.diamond
        collection_series = db.series
        collection_features = db.features

        args = request.args.to_dict(flat=True)

        data = list(collection_series.find(args))
        response = []
        for row in data:
            features = row.get("features", [])
            if features:
                features_data = collection_features.find({"_id": {"$in": features}})
                response.append(list(features_data))

    response = jsonify({"data": response})
    return response


def create_data(data):
    with current_app.app_context():
        db = current_app.mongo_client.diamond
        collection_series = db.series
        collection_features = db.features

        series_code = data.get("seriesCode")
        features = data.get("features")

        feature_ids = []
        for feature in features:

            feature_code = feature.get("featureCode")
            features_list = list(collection_features.find({"featureCode": feature_code}))
            if len(features_list) > 0:
                collection_features.update_one(
                    {"featureCode": feature_code}, {"$set": feature}
                )
                feature_ids.append(features_list[0]["_id"])
            else:
                if "_id" not in feature:
                    feature["_id"] = str(uuid.uuid4())
                inserted_obj = collection_features.insert_one(feature)
                feature_ids.append(inserted_obj.inserted_id)

        series_list = list(collection_series.find({"seriesCode": series_code}))
        if len(series_list) > 0:
            for series in series_list:
                added_feature_ids = series["features"]
                unique_features_ids = list(set(added_feature_ids + feature_ids))
                collection_series.update_one(
                    {"seriesCode": series_code}, {"$set": {"features": unique_features_ids}}
                )

    response = jsonify({"message": "Data inserted successfully"})
    return response
