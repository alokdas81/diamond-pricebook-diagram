import urllib

MONGO_URI = (
    "mongodb+srv://"
    + urllib.parse.quote("ogma")
    + ":"
    + urllib.parse.quote("ogma123")
    + "@pricebookcluster.fpwwf4a.mongodb.net/?retryWrites=true&w=majority"
)
