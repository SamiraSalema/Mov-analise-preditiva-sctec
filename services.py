import pandas as pd

NOMES_VARIAVEIS = [
    "galerias_arte",
    "clubes_danca",
    "bares_sucos",
    "restaurantes",
    "museus",
    "resorts",
    "parques_picnic",
    "praias",
    "teatros",
    "instituicoes_religiosas"
]


def prever_grupo(modelo, preferencias):
    dados = preferencias.model_dump()

    entrada = pd.DataFrame(
        [dados],
        columns=NOMES_VARIAVEIS
    )

    grupo = int(modelo.predict(entrada)[0])

    return {
        "grupo": grupo,
        "mensagem": (
            f"Preferências classificadas no grupo {grupo}."
        )
    }
