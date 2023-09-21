from flask import current_app, jsonify, request
import uuid
from app.utils import get_utc_time

def get_data():
    with current_app.app_context():
        db = current_app.mongo_client.diamond
        collection_series = db.series
        collection_adon_features = db.adonFeatures

        args = request.args.to_dict(flat=True)

        data = list(collection_series.find(args))
        response = []
        for row in data:
            adon_features = row.get("adonFeatures", [])
            if adon_features:
                adon_features_data = collection_adon_features.find(
                    {"_id": {"$in": adon_features}}
                )
                row["adonFeatures"] = list(adon_features_data)
                if "features" in row:
                    del row["features"]
                response.append(row)

    response = jsonify({"data": response})
    return response


def create_data(data):
    with current_app.app_context():
        db = current_app.mongo_client.diamond
        collection_series = db.series
        collection_adon_features = db.adonFeatures

        data = request.json
        series_code = data.get("seriesCode")
        adon_features = data.get("adonFeatures")

        adon_features_ids = []
        for adon_feature in adon_features:

            adon_feature_code = adon_feature.get("adonFeatureCode")
            adon_feature_list = list(
                collection_adon_features.find({"adonFeatureCode": adon_feature_code})
            )
            if len(adon_feature_list) > 0:
                adon_feature["updatedAt"] = get_utc_time()
                collection_adon_features.update_one(
                    {"adonFeatureCode": adon_feature_code}, {"$set": adon_feature}
                )
                adon_features_ids.append(adon_feature_list[0]["_id"])
            else:
                if "_id" not in adon_feature:
                    adon_feature["_id"] = str(uuid.uuid4())
                adon_feature["createdAt"] = get_utc_time()
                adon_feature["updatedAt"] = get_utc_time()
                inserted_obj = collection_adon_features.insert_one(adon_feature)
                adon_features_ids.append(inserted_obj.inserted_id)

        series_list = list(collection_series.find({"seriesCode": series_code}))
        if len(series_list) > 0:
            for series in series_list:
                added_adon_features_ids = series["adonFeatures"]
                unique_adon_features_ids = list(
                    set(added_adon_features_ids + adon_features_ids)
                )

                collection_series.update_one(
                    {"seriesCode": series_code},
                    {"$set": {"adonFeatures": unique_adon_features_ids}},
                )

    response = jsonify({"message": "Data inserted successfully"})
    return response
