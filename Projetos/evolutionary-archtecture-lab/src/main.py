from fastapi import FastAPI
from src.modules.events.router import router as events_router

app = FastAPI(title="Evolutionary Architecture Lab")

# Registro do módulo
app.include_router(events_router, prefix="/events", tags=["Events"])

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API do Lab de Arquitetura!"}