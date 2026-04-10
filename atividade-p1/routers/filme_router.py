from fastapi import APIRouter
from app.schemas.filme_schema import Filme
from app.services.filme_service import *

router = APIRouter()

@router.get("/filmes")
def list_filmes():
    return get_all_filmes_service()

@router.post("/filmes")
def create_filme(filme: Filme):
    return create_filme_service(filme)

@router.get("/filmes/{filme_id}")
def get_filme(filme_id: str):
    return get_filme_by_id_service(filme_id)

@router.put("/filmes/{filme_id}")
def update_filme(filme_id: str, filme: Filme):
    return update_filme_service(filme_id, filme)

@router.delete("/filmes/{filme_id}")
def delete_filme(filme_id: str):
    return delete_filme_service(filme_id)
