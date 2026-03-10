from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.database import get_db
from src.modules.events.schemas.event_schema import EventCreate, EventResponse
from src.modules.events.repository.event_repository import EventRepository

router = APIRouter()


@router.post("/", response_model=EventResponse)
def create_event(event_data: EventCreate, db: Session = Depends(get_db)):
    # 1. Instanciamos o repositório com a sessão do banco
    repository = EventRepository(db)

    # 2. Chamamos o método de criação
    # .model_dump() transforma o schema do Pydantic em um dicionário Python
    new_event = repository.create(event_data.model_dump())

    return new_event


@router.get("/", response_model=List[EventResponse])
def list_events(db: Session = Depends(get_db)):
    repository = EventRepository(db)
    return repository.get_all()