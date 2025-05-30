# API de Previsão de Preços de Imóveis

![Python](https://img.shields.io/badge/Python-Interpreted-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?style=flat-square&logo=flask)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Machine%20Learning-orange?style=flat-square&logo=scikitlearn)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-blue?style=flat-square&logo=pandas)
![API REST](https://img.shields.io/badge/API-REST-green?style=flat-square)
![Thunder Client](https://img.shields.io/badge/Thunder--Client-Tested-purple?style=flat-square)


## Descrição

Este projeto consiste em uma API REST desenvolvida em Python utilizando o microframework Flask. A API tem como finalidade realizar previsões de preços de imóveis com base em três características principais: tamanho do imóvel (em m²), ano de construção e número de vagas de garagem.

O modelo de machine learning utilizado é uma Regressão Linear, treinado com a biblioteca scikit-learn. Os dados foram processados com a biblioteca Pandas e o modelo foi serializado utilizando o módulo `pickle` para reaproveitamento em produção.

A API foi projetada para ser simples, intuitiva e segura, utilizando autenticação básica (`BasicAuth`) para proteger o endpoint principal de previsões. O endpoint aceita requisições do tipo POST com dados em formato JSON e retorna o preço estimado com duas casas decimais de precisão.

Essa aplicação é ideal para fins didáticos e demonstra como integrar modelos de machine learning com APIs web, permitindo sua utilização em sistemas reais como sites, aplicativos móveis ou serviços internos.

---

## Funcionalidades

- [x] Carregamento de modelo treinado com pickle
- [x] API REST desenvolvida com Flask
- [x] Previsão de preço de imóvel com base em:
  - Tamanho (em metros quadrados)
  - Ano de construção
  - Número de vagas na garagem
- [x] Proteção do endpoint com autenticação básica (`BasicAuth`)
- [x] Retorno formatado do preço previsto com arredondamento
- [x] Tratamento de erros e respostas padronizadas
- [x] Testes locais com Thunder Client
- [x] Código modularizado com separação de responsabilidades
- [x] Leitura e pré-processamento de dados com Pandas
- [x] Validação dos dados de entrada via estrutura de dicionário
- [x] Ambiente virtual configurado com `venv`
- [x] Requisições JSON com resposta em formato legível
- [x] Aplicação executável localmente via `python main.py`

---

## Tecnologias Utilizadas

- **Python 3.11**: Linguagem de programação principal usada no desenvolvimento do projeto.
- **Flask 2.3**: Microframework para construção de APIs web de forma simples e eficiente.
- **scikit-learn 1.4**: Biblioteca de aprendizado de máquina utilizada para criar e treinar o modelo de regressão linear.
- **Pandas 2.2.2**: Biblioteca para manipulação e análise de dados estruturados, utilizada para leitura e preparação do dataset.
- **Pickle (módulo padrão)**: Utilizado para serializar e desserializar o modelo de machine learning treinado.
- **Thunder Client**: Ferramenta integrada ao VSCode usada para testar endpoints HTTP.
