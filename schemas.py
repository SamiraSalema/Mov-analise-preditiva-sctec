from pydantic import BaseModel, Field, ConfigDict


class PreferenciasTurista(BaseModel):
    model_config = ConfigDict(extra="forbid")

    galerias_arte: float = Field(ge=0, le=4)
    clubes_danca: float = Field(ge=0, le=4)
    bares_sucos: float = Field(ge=0, le=4)
    restaurantes: float = Field(ge=0, le=4)
    museus: float = Field(ge=0, le=4)
    resorts: float = Field(ge=0, le=4)
    parques_picnic: float = Field(ge=0, le=4)
    praias: float = Field(ge=0, le=4)
    teatros: float = Field(ge=0, le=4)
    instituicoes_religiosas: float = Field(ge=0, le=4)


class ResultadoPredicao(BaseModel):
    grupo: int
    mensagem: str
