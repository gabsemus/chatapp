import streamlit as st

def opcao_produto(produto_nome, produto_descricao, produto_preco, key):

   container = st.container()
   with container:
      with st.empty():
         st.write('')

      col1, col2 = st.columns(2)
      with col1:
         st.text(produto_nome)
         st.text(produto_descricao)
         st.text(f'valor: R$ {produto_preco}')

      with col2:
         quantidade_produto = st.number_input(label='', min_value = 0, step=1, key = key)

      retorno = {}
      retorno['prduto'] = produto_nome
      retorno['quantidade'] = quantidade_produto

   return retorno
