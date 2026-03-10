from sqlalchemy.orm import Session
from .models import EventModel

class EventRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, event_data: dict):
        db_event = EventModel(**event_data)
        self.db.add(db_event)
        self.db.commit()
        self.db.refresh(db_event)
        return db_event

    def get_all(self):
        return self.db.query(EventModel).all()