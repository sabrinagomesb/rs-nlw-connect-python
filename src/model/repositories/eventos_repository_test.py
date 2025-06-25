import pytest
from .eventos_repository import EventosRepository

@pytest.mark.skip("test_insert_event")
def test_insert_event():
    event_name = "Test Event"
    event_repo = EventosRepository()

    event_repo.insert(event_name)

def test_get_event():
    event_name = "Test Event"
    event_repo = EventosRepository()

    event = event_repo.get_event(event_name)
    print(event)
    print(event.nome)


