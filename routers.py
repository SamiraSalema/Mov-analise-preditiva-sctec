from fastapi import APIRouter, Request, HTTPException
from schemas import PreferenciasTurista, ResultadoPredicao
from services import prever_grupo

router = APIRouter()

@router.get("/health")
def verificar_saude(request: Request):
    modelo = getattr(request.app.state, "modelo", None)

    return {
        "status": "ativo" if modelo is not None else "indisponivel",
        "modelo_carregado": modelo is not None
    }

@router.post("/predict", response_model=ResultadoPredicao)
def realizar_predicao(
    preferencias: PreferenciasTurista,
    request: Request
):
    modelo = getattr(request.app.state, "modelo", None)

    if modelo is None:
        raise HTTPException(
            status_code=503,
            detail="Modelo indisponível."
        )

    return prever_grupo(modelo, preferencias)
