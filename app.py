from pymongo import MongoClient
from flask import Flask

client = MongoClient('localhost', 27017)
db = client.test_database
app = Flask(__name__)

@app.route("/")
def hello():
    return "Olar"

if __name__ == "__main__":
    app.run()
