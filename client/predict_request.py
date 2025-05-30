import requests
from requests.auth import HTTPBasicAuth

def consultar_preco(tamanho, ano, garagem, url="http://127.0.0.1:5000/cotacao/"):
  dados = {
    "tamanho": tamanho,
    "ano": ano,
    "garagem": garagem
  }

  try:
    response = requests.post(url, json=dados, auth=HTTPBasicAuth('admin', 'teste')) # Autenticação básica
    response.raise_for_status()  # Levanta um erro para códigos de status HTTP 4xx/5xx
    return response.json()
  except requests.exceptions.RequestException as e:
    return {"error": str(e)}

    