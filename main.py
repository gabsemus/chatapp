import streamlit as st

from paginas.cadastro_usuario import cadastrar_usuario
from paginas.home import home
from paginas.registrar_entrada import entrada_usuario
from paginas.registrar_pedido import realizar_pedido
from paginas.saldo_cliente import consultar_saldo

page_names_to_funcs = {
   "Home": home,
   "Cadastro do Usuário": cadastrar_usuario,
   "Registrar Entrada": entrada_usuario,
   "Registrar Pedido": realizar_pedido,
   "Saldo do Cliente": consultar_saldo
}

demo_name = st.sidebar.selectbox("Selecione a página", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()