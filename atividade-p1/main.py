from fastapi import FastAPI
from app.routers.filme_router import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def home():
    return {"Message": "FastAPI + MongoDB + Docker: CRUD de Filmes"}
