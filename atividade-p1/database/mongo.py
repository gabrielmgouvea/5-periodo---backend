import os
from pymongo import MongoClient

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27018")

client = MongoClient(MONGO_URL)

db = client["exercicio_backend"]

filmes_collection = db["filmes"]
