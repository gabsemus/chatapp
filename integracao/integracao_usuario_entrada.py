import requests


def integracao_entrada(nome, comanda, celular):
   url = 'https://nooru9bm2i.execute-api.us-east-1.amazonaws.com/default/cassio_backend/registrar_entrada'
   payload = {}
   payload['nome'] = nome
   payload['comanda'] = comanda
   payload['celular'] = celular
   r = requests.post(url, json=payload)
   return r
