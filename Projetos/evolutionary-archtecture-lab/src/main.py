from fastapi import FastAPI
from src.modules.events.router import router as events_router
from src.database import engine, Base
# Importar o model para o SQLAlchemy "conhecer" a tabela
from src.modules.events.repository import models

# Cria as tabelas se não existirem
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Evolutionary Architecture Lab")

# Registro do módulo
app.include_router(events_router, prefix="/events", tags=["Events"])

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API do Lab de Arquitetura!"}