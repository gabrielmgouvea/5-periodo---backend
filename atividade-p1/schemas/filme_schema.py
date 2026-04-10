from pydantic import BaseModel

class Filme(BaseModel):
    titulo: str
    diretor: str
    ano: int
    genero: str
