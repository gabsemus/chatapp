import streamlit as st

from integracao.integracao_usuario import integracao_usuario


def cadastrar_usuario():
   st.subheader('Cadastro do Cliente')

   with st.form("CadastroUsuario"):
      st.write("Cadastro do Cliente")
      usuario_nome = st.text_input("Nome: ", placeholder = 'Informe o nome do cliente')
      usuario_celular = st.text_input("Celular", help = 'Informe o DDD + Número' ,placeholder = 'Informe o celular do cliente')


      submitted = st.form_submit_button("Salvar")
      if submitted:
         integracao_usuario(usuario_nome,usuario_celular)
         st.write(f'Registro Salvo!')