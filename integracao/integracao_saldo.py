import requests

def integracao_consultar_saldo(payload):
   url = 'https://nooru9bm2i.execute-api.us-east-1.amazonaws.com/default/cassio_backend/saldo/2'
   r = requests.get(url, json=payload)
   retorno = r.json()
   return retorno
