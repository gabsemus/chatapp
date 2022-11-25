import requests


def integracao_pedido(payload):
   url = 'https://nooru9bm2i.execute-api.us-east-1.amazonaws.com/default/cassio_backend/cadastro_usuario'
   r = requests.post(url, json=payload)
   return r
