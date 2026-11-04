
# MOv — Análise de Preferências Turísticas

**Projeto Final — Desenvolvimento de IA para Análise Preditiva | SCTEC**

## 1. Apresentação

O MOv é um projeto experimental de Machine Learning desenvolvido para investigar padrões de preferências turísticas a partir de dados de avaliações de usuários.

A proposta é explorar como técnicas de Inteligência Artificial podem contribuir futuramente para a personalização de experiências na plataforma MOv, idealizada para o turismo em Navegantes, Santa Catarina.

Nesta etapa, o projeto contempla análise exploratória, treinamento de modelo não supervisionado, avaliação de agrupamentos e disponibilização de uma API para consulta dos resultados.

## 2. Objetivo

Desenvolver um protótipo capaz de identificar agrupamentos de usuários com características semelhantes de preferências turísticas, utilizando o algoritmo K-Means.

O projeto constitui um estudo exploratório de segmentação, sem previsão de destinos ou geração automática de recomendações.

## 3. Base de dados

Foi utilizada a base pública **Travel Reviews**, disponibilizada pelo UCI Machine Learning Repository.

- **Fonte:** [UCI — Travel Reviews](https://archive.ics.uci.edu/dataset/484/travel+reviews)
- **Arquivo:** `data/tripadvisor_review.csv`
- **Registros:** 980
- **Variáveis de preferência:** 10
- **Identificador adicional:** User ID
- **Valores ausentes:** nenhum identificado

As variáveis representam avaliações de diferentes categorias de estabelecimentos e atrações turísticas.

**Observação:** a base não contém dados específicos de visitantes de Navegantes. Sua utilização tem finalidade acadêmica e experimental.

## 4. Metodologia

O desenvolvimento foi organizado nas seguintes etapas:

1. Carregamento e análise exploratória dos dados.
2. Verificação da qualidade da base.
3. Preparação das dez variáveis de preferência.
4. Divisão dos registros em treinamento (60%), validação (20%) e teste (20%).
5. Padronização dos dados com `StandardScaler`, ajustado no treinamento.
6. Avaliação do algoritmo K-Means com valores de K entre 2 e 8.
7. Seleção de dois agrupamentos com base na avaliação de validação.
8. Avaliação final com dados de teste.
9. Serialização do modelo com Joblib.
10. Integração do modelo à API FastAPI.

O artefato salvo utiliza um Pipeline composto por `StandardScaler` e `KMeans`.

## 5. Resultados

| Métrica | Resultado |
|---|---|
| Silhouette — validação | 0.1866 |
| Silhouette — teste | 0.2185 |
| Número de clusters | 2 |
| Registros no grupo 0 — base completa | 404 |
| Registros no grupo 1 — base completa | 576 |

Os resultados indicam uma separação relativamente fraca entre os agrupamentos.

Assim, a segmentação deve ser interpretada como um resultado exploratório, que ainda necessita de validação e aprimoramento antes de qualquer aplicação comercial.

As métricas estão disponíveis em `reports/metricas_modelo.json`.

## 6. Estrutura do projeto

```text
Mov-analise-preditiva-sctec/
├── data/
│   └── tripadvisor_review.csv
├── models/
│   └── mov_kmeans_pipeline.joblib
├── notebooks/
│   └── MOv_Analise_Preditiva_SCTEC (2).ipynb
├── reports/
│   └── metricas_modelo.json
├── main.py
├── routers.py
├── schemas.py
├── services.py
├── test_api.py
├── requirements.txt
└── README.md
```

## 7. Tecnologias utilizadas

- **Python:** linguagem principal
- **Pandas e NumPy:** manipulação e análise de dados
- **Scikit-learn:** pré-processamento, treinamento e avaliação
- **Joblib:** persistência do modelo
- **FastAPI:** desenvolvimento da API
- **Pydantic:** validação dos dados
- **Uvicorn:** servidor ASGI
- **Pytest:** testes automatizados

## 8. Instalação e configuração

Pré-requisitos: Python e Git instalados.

Clone o repositório:

```bash
git clone https://github.com/SamiraSalema/Mov-analise-preditiva-sctec.git
```

Acesse a pasta:

```bash
cd Mov-analise-preditiva-sctec
```

Crie o ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual.

**Windows (Prompt de Comando):**

```bat
.venv\Scripts\activate.bat
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

## 9. Executando a API

Na pasta principal do projeto, execute:

```bash
uvicorn main:app --reload
```

Após iniciar o servidor, acesse:

- **Swagger:** http://127.0.0.1:8000/docs
- **Health:** http://127.0.0.1:8000/health
- **OpenAPI:** http://127.0.0.1:8000/openapi.json

Os endereços são locais e exigem que a API esteja em execução.

## 10. Endpoints

### GET /health

Verifica a disponibilidade da API e o carregamento do modelo.

Exemplo de resposta:

```json
{
  "status": "ativo",
  "modelo_carregado": true
}
```

### POST /predict

Recebe dez valores de preferências turísticas, dentro do intervalo de 0 a 4, e retorna o grupo atribuído pelo modelo.

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

Exemplo de resposta observada:

```json
{
  "grupo": 0,
  "mensagem": "Preferências classificadas no grupo 0."
}
```

O número do grupo representa um agrupamento identificado pelo modelo, não uma classificação de qualidade turística.

## 11. Validação e testes

A API utiliza Pydantic para validar os dados recebidos.

Foram verificados os seguintes códigos HTTP:

- **200:** operação bem-sucedida
- **404:** rota inexistente
- **422:** dados de entrada inválidos
- **503:** modelo indisponível
- **500:** erro interno inesperado

Para executar os testes automatizados:

```bash
python -m pytest -v
```

**Resultado:** quatro testes automatizados aprovados, contemplando disponibilidade da API, predição e validação de entradas.

## 12. Limitações e melhorias futuras

O projeto apresenta limitações importantes:

- A base não representa diretamente os visitantes de Navegantes.
- Os agrupamentos apresentam separação relativamente fraca.
- O modelo não prevê destinos nem produz recomendações personalizadas.
- Os resultados não comprovam a utilidade comercial da segmentação.

Como possibilidades de evolução, destacam-se a coleta de dados locais, a investigação de novas variáveis, a comparação de algoritmos e a avaliação dos perfis com usuários reais.

## 13. Vídeo de demonstração

Link:https://youtu.be/oSwKYpeQrA0

O vídeo apresentará o objetivo do projeto, a metodologia, os resultados, a estrutura do código, a API e os testes realizados.

## 14. Autoria

**Samira Salema**

Projeto acadêmico desenvolvido no âmbito do SCTEC — Desenvolvimento de IA para Análise Preditiva.

**Repositório:** [MOv — GitHub](https://github.com/SamiraSalema/Mov-analise-preditiva-sctec)
