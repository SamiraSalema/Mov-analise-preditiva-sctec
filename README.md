# MOv — Análise de Preferências Turísticas

Projeto Final — Desenvolvimento de IA para Análise Preditiva | SCTEC

## 1. Objetivo

Desenvolver um protótipo de Machine Learning capaz de
identificar agrupamentos de preferências turísticas,
como estudo inicial para a futura plataforma MOv,
voltada à personalização de experiências em
Navegantes, Santa Catarina.

## 2. Base de dados

- Arquivo: `data/tripadvisor_review.csv`
- Registros: 980
- Variáveis de preferência: 10
- Identificador adicional: User ID
- Referência pública: Travel Reviews — UCI Machine Learning Repository
- Link: https://archive.ics.uci.edu/dataset/484/travel+reviews

A base não representa especificamente visitantes de Navegantes.
O projeto tem caráter experimental.

## 3. Metodologia

- Análise exploratória dos dados
- Divisão: 60% treinamento, 20% validação, 20% teste
- Padronização com StandardScaler
- Agrupamento não supervisionado com K-Means
- Avaliação de K entre 2 e 8
- Seleção de 2 clusters
- Serialização com Joblib

O modelo salvo utiliza um Pipeline com StandardScaler e KMeans.

## 4. Resultados

| Métrica | Resultado |
|---|---|
| Silhouette de validação | 0.1866 |
| Silhouette de teste | 0.2185 |
| Número de clusters | 2 |
| Registros no grupo 0 | 404 |
| Registros no grupo 1 | 576 |

Os resultados indicam separação relativamente fraca entre
os agrupamentos. A segmentação deve ser interpretada
como um protótipo exploratório, não como uma
recomendação turística já validada.

Métricas detalhadas: `reports/metricas_modelo.json`.

## 5. Estrutura do projeto

```text
data/
    tripadvisor_review.csv
models/
    mov_kmeans_pipeline.joblib
reports/
    metricas_modelo.json
main.py
routers.py
schemas.py
services.py
test_api.py
requirements.txt
README.md
```

O notebook de treinamento também deverá ser incluído
no repositório final.

## 6. Tecnologias

- Python
- Pandas e NumPy
- Scikit-learn
- Joblib
- FastAPI
- Pydantic
- Uvicorn
- Pytest

## 7. Instalação

Requisitos: Python e Git instalados.

Clone o repositório e entre na pasta do projeto.

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual.

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

## 8. Executar a API

Na pasta principal do projeto:

```bash
uvicorn main:app --reload
```

Acesse:

- Swagger: http://127.0.0.1:8000/docs
- Health: http://127.0.0.1:8000/health
- OpenAPI: http://127.0.0.1:8000/openapi.json

## 9. Endpoints

### GET /health

Verifica se o modelo está carregado na memória.

Resposta de exemplo:

```json
{
  "status": "ativo",
  "modelo_carregado": true
}
```

### POST /predict

Recebe dez valores de preferências turísticas
e retorna o grupo atribuído pelo modelo.

Exemplo de requisição:

```json
{
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
```

Resposta observada:

```json
{
  "grupo": 0,
  "mensagem": "Preferências classificadas no grupo 0."
}
```

## 10. Validação e testes

A API utiliza Pydantic para validar os dados de entrada.

Códigos HTTP verificados:

- 200: operação bem-sucedida
- 404: rota inexistente
- 422: entrada inválida
- 503: modelo indisponível
- 500: erro interno inesperado

Para executar os testes automatizados:

```bash
python -m pytest -v
```

Foram aprovados quatro testes automatizados.

## 11. Limitações e melhorias futuras

- A base não representa diretamente o turismo de Navegantes.
- A separação entre clusters é relativamente fraca.
- O modelo identifica agrupamentos, não prevê destinos
  nem garante recomendações personalizadas.
- Coletar dados próprios de visitantes.
- Investigar novas variáveis e algoritmos.
- Relacionar perfis a atrações e experiências locais.
- Avaliar a utilidade das recomendações com usuários reais.

## 12. Vídeo de demonstração

Link: a inserir após a gravação e publicação.

## 13. Desenvolvimento

Projeto acadêmico desenvolvido no âmbito do SCTEC.
