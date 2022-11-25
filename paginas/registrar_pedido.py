import streamlit as st

from elementos.criar_produto import opcao_produto
from elementos.criar_pedido import criar_pedido_integracao
from integracao.integracao_pedido import integracao_pedido

def realizar_pedido():

   st.subheader('Registrar Pedido')

   with st.form("RegistrarPedido"):
      st.write("Registrar Pedido")

      usuario_comanda = st.selectbox(label="Pulseira: ", options = ('1', '2', '3'), help  = 'Informe o nome do cliente')

      skol = opcao_produto('Skol Litão', 'Melhor Cerveja Ever', '20', 'skol')

      brahma = opcao_produto('Brahma Litão', '2° Melhor Cerveja Ever', '20', 'brahma')

      produtos = [skol, brahma]

      submitted = st.form_submit_button("Salvar")

      if submitted:
         integracao_pedido(
            criar_pedido_integracao(usuario_comanda, produtos)
         )
         st.write('Registro Salvo!')
