import streamlit as st

from integracao.integracao_usuario_entrada import integracao_entrada


def entrada_usuario():
   st.subheader('Registrar Entrada')

   with st.form("RegistrarEntrada"):
      st.write("Entrada do Cliente")
      usuario_nome = st.text_input(label="Nome: ", placeholder  = 'Informe o nome do cliente')

      usuario_comanda = st.text_input("Pulseira", placeholder = 'Informe o número da pulseira')

      usuario_celular = st.text_input("Celular", help = 'Informe o DDD + Número' ,placeholder = 'Informe o celular do cliente')

      submitted = st.form_submit_button("Salvar")

      if submitted:
         integracao_entrada(usuario_nome, usuario_comanda, usuario_celular)
         st.write('Registro Salvo!')