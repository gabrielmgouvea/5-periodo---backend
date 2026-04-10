from app.repositories.filme_repository import *
from bson import ObjectId

def format_filme(filme):
    filme["_id"] = str(filme["_id"])
    return filme

def get_all_filmes_service():
    filmes = get_all_filmes()
    return [format_filme(filme) for filme in filmes]

def create_filme_service(filme):
    result = create_filme(filme.model_dump())
    return {"message": "Filme Criado", "id": str(result.inserted_id)}

def get_filme_by_id_service(filme_id):
    try:
        filme = get_filme_by_id(filme_id)
    except:
        return {"error": "Id inválido"}
    
    if not filme:
        return {"error": "Filme não encontrado"}
    return format_filme(filme)

def update_filme_service(filme_id, filme):
    try:
        result = update_filme(filme_id, filme.model_dump())
    except:
        return {"error": "ID inválido"}
    if result.matched_count == 0:
        return {"error": "Filme não encontrado"}
    return {"message": "Filme atualizado"}

def delete_filme_service(filme_id):
    try:
        result = delete_filme(filme_id)
    except:
        return {"error": "Filme não encontrado"}
    return {"message": "Filme deletado"}
