from fastapi import APIRouter, HTTPException
from src.modules.events.schemas.event_schema import EventCreate, EventResponse

router = APIRouter()

# Simulando um banco de dados em memória por enquanto
fake_db = []


@router.post("/", response_model=EventResponse)
def create_event(event_data: EventCreate):
    # Aqui, no futuro, chamaremos o "Service"
    new_event = event_data.model_dump()
    from uuid import uuid4
    new_event["id"] = uuid4()
    new_event["is_published"] = False

    fake_db.append(new_event)
    return new_event


@router.get("/")
def list_events():
    return fake_db