from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.database import get_db
from src.modules.events.schemas.event_schema import EventCreate, EventResponse
from src.modules.events.services.event_service import EventService # Importamos o Service

router = APIRouter()

@router.post("/", response_model=EventResponse)
def create_event(event_data: EventCreate, db: Session = Depends(get_db)):
    service = EventService(db)
    try:
        # O Router agora só pede para o Service: "Crie este evento para mim"
        return service.create_event(event_data)
    except ValueError as e:
        # Tratamento de erro de regra de negócio transformado em erro HTTP
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[EventResponse])
def list_events(db: Session = Depends(get_db)):
    service = EventService(db)
    return service.list_all()