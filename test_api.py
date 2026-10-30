
from fastapi.testclient import TestClient
from main import app

EXEMPLO = {
    "galerias_arte": 3.0,
    "clubes_danca": 1.0,
    "bares_sucos": 2.0,
    "restaurantes": 4.0,
    "museus": 3.0,
    "resorts": 2.0,
    "parques_picnic": 4.0,
    "praias": 4.0,
    "teatros": 2.0,
    "instituicoes_religiosas": 1.0
}

def test_health():
    with TestClient(app) as cliente:
        resposta = cliente.get("/health")
        assert resposta.status_code == 200
        assert resposta.json()["modelo_carregado"] is True

def test_predict():
    with TestClient(app) as cliente:
        resposta = cliente.post("/predict", json=EXEMPLO)
        assert resposta.status_code == 200
        assert isinstance(resposta.json()["grupo"], int)

def test_valor_invalido():
    dados = EXEMPLO.copy()
    dados["praias"] = -1

    with TestClient(app) as cliente:
        resposta = cliente.post("/predict", json=dados)
        assert resposta.status_code == 422

def test_campo_extra():
    dados = EXEMPLO.copy()
    dados["categoria_inexistente"] = 2.0

    with TestClient(app) as cliente:
        resposta = cliente.post("/predict", json=dados)
        assert resposta.status_code == 422
