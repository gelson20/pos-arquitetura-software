from sqlalchemy.orm import Session
from src.modules.events.repository.event_repository import EventRepository
from src.modules.events.schemas.event_schema import EventCreate
from datetime import datetime, timezone

class EventService:
    def __init__(self, db: Session):
        self.repository = EventRepository(db)

    def create_event(self, event_data: EventCreate):
        # Exemplo de Regra de Negócio: Não permitir eventos no passado
        if event_data.date < datetime.now(timezone.utc):
            raise ValueError("A data do evento não pode ser no passado.")

        # Transformamos o schema em dicionário e passamos para o repositório
        return self.repository.create(event_data.model_dump())

    def list_all(self):
        return self.repository.get_all()