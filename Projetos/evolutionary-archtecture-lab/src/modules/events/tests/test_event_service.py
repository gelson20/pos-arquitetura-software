import pytest
from datetime import datetime, timedelta, timezone
from unittest.mock import MagicMock
from src.modules.events.services.event_service import EventService
from src.modules.events.schemas.event_schema import EventCreate


def test_deve_impedir_criacao_de_evento_no_passado():
    # 1. Setup (Simulamos o banco de dados para não precisar de um real)
    mock_db = MagicMock()
    service = EventService(db=mock_db)

    # Criamos uma data de ontem
    data_passada = datetime.now(timezone.utc) - timedelta(days=1)

    event_dto = EventCreate(
        name="Evento Inválido",
        date=data_passada,
        location="Qualquer lugar",
        description="Teste de erro"
    )

    # 2. Execução & Verificação
    # Esperamos que o service levante um ValueError
    with pytest.raises(ValueError) as excinfo:
        service.create_event(event_dto)

    assert str(excinfo.value) == "A data do evento não pode ser no passado."


def test_deve_permitir_criacao_de_evento_no_futuro():
    mock_db = MagicMock()
    service = EventService(db=mock_db)

    # Criamos uma data para amanhã
    data_futura = datetime.now(timezone.utc) + timedelta(days=1)

    event_dto = EventCreate(
        name="Evento Válido",
        date=data_futura,
        location="Curitiba",
        description="Show de Rock"
    )

    # Execução (Não deve dar erro)
    service.create_event(event_dto)

    # Verificamos se o repositório foi chamado pelo menos uma vez
    assert mock_db.add.called