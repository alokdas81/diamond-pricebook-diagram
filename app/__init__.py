from flask import Flask
from pymongo import MongoClient

def create_app(config_filename="config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)
    
    # Initialize MongoDB client
    mongo_client = MongoClient(app.config["MONGO_URI"])
    app.mongo_client = mongo_client

    # Register API blueprints
    from app.routes.manufacturer import manufacturer
    from app.routes.brand import brand
    from app.routes.series import series
    from app.routes.feature import feature
    from app.routes.adon_feature import adonFeature
    from app.routes.baseprice import baseprice

    app.register_blueprint(manufacturer)
    app.register_blueprint(brand)
    app.register_blueprint(series)
    app.register_blueprint(feature)
    app.register_blueprint(adonFeature)
    app.register_blueprint(baseprice)

    return app
