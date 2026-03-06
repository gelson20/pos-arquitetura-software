from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from uuid import UUID

class EventCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    date: datetime
    location: str
    description: Optional[str] = None

class EventResponse(BaseModel):
    id: UUID
    name: str
    date: datetime
    location: str
    is_published: bool

    class Config:
        from_attributes = True # Permite converter o modelo do banco para o schema