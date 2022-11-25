import requests


def integracao_usuario(nome, celular):
   url = 'https://nooru9bm2i.execute-api.us-east-1.amazonaws.com/default/cassio_backend/cadastro_usuario'
   payload = {}
   payload['nome'] = nome
   payload['celular'] = celular
   r = requests.post(url, json=payload)
   return r
