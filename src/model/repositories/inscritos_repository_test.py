import pytest
from.inscritos_repository import InscritosRepository

@pytest.mark.skip("Insert in DB")
def test_insert():
    dados_inscrito = {
        "nome": "Test Subscriber",
        "email": "test@mail.com",
        # "link": "http://example.com",
        "evento_id": 1
    }
    repository = InscritosRepository()
    repository.insert(dados_inscrito)

def test_get_subscriber():
    email = "test@mail.com"
    evento_id = 1

    repository = InscritosRepository()
    resposta = repository.get_subscriber(email, evento_id)
    print(resposta.nome)
