from contextlib import asynccontextmanager
from pathlib import Path

import joblib
from fastapi import FastAPI
from routers import router

BASE_DIR = Path(__file__).resolve().parent
CAMINHO_MODELO = BASE_DIR / "models" / "mov_kmeans_pipeline.joblib"

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.modelo = joblib.load(CAMINHO_MODELO)
    try:
        yield
    finally:
        app.state.modelo = None

app = FastAPI(
    title="MOv - Análise de Preferências Turísticas",
    description="API para agrupamento de perfis turísticos.",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(router)
