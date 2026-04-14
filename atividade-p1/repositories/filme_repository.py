from app.database.mongo import filmes_collection
from bson import ObjectId

def create_filme(filme_dict):
    return filmes_collection.insert_one(filme_dict)

def get_all_filmes():
    return list(filmes_collection.find())

def get_filme_by_id(filme_id):
    return filmes_collection.find_one({"_id": ObjectId(filme_id)})

def update_filme(filme_id, filme_dict):
    return filmes_collection.update_one(
        {"_id": ObjectId(filme_id)},
        {"$set": filme_dict}
    )

def delete_filme(filme_id):
    return filmes_collection.delete_one(
        {"_id": ObjectId(filme_id)}
    )
