from sqlalchemy import Column, String, DateTime, Boolean
from src.database import Base
import uuid

# Helper para gerar IDs em formato string
def generate_uuid():
    return str(uuid.uuid4())

class EventModel(Base):
    __tablename__ = "events"

    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    location = Column(String, nullable=False)
    description = Column(String, nullable=True)
    is_published = Column(Boolean, default=False)