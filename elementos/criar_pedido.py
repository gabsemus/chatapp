def criar_pedido_integracao(comanda, itens_pedido):
   payload = {}
   itens = []

   payload['comanda'] = comanda

   for item in itens_pedido:
      if item['quantidade'] > 1:
         itens.append(item)

   payload['itens'] = itens

   return payload
