# Football Data Analysis

Projeto de coleta, tratamento e análise de dados de futebol utilizando Python.

## Objetivo

O projeto tem como objetivo construir uma base de dados estruturada a partir de informações de competições e partidas de futebol, permitindo realizar análises estatísticas posteriormente.

O desenvolvimento será realizado por etapas, começando pela coleta e tratamento dos dados.

## Tecnologias

* Python
* Pandas
* Requests
* REST API
* CSV

## Etapas do projeto

### 1. Coleta e tratamento dos dados

* Consumo da API `football-data.org`
* Coleta de tabelas de classificação
* Coleta de partidas
* Tratamento dos dados retornados em JSON
* Conversão para DataFrames
* Tratamento de datas
* Separação de partidas finalizadas
* Exportação dos dados para CSV

### 2. Análise dos dados

Em desenvolvimento.

### 3. Visualização dos dados

Em desenvolvimento.

## Estrutura

```text
football-data-analysis/
│
├── coleta_dados.py
├── config.py
├── *.csv
└── README.md
```

## Fonte dos dados

Os dados utilizados no projeto são obtidos através da API do [football-data.org](https://www.football-data.org/).

## Status

🚧 Projeto em desenvolvimento.
