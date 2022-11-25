import streamlit as st

from integracao.integracao_saldo import integracao_consultar_saldo


def consultar_saldo():
   st.subheader('Conta do Cliente')

   with st.form("SaldoUsuario"):
      st.write("Visualizar o saldo do cliente")

      usuario_comanda = st.text_input("Pulseira", placeholder = 'Informe o número da pulseira')

      submitted = st.form_submit_button("Ver Saldo")
      if submitted:
          conta_corrente = integracao_consultar_saldo(usuario_comanda)

          total_comanda = 0

          for item in conta_corrente['itens']:
              produto = item['produto']
              quantidade = item['quantidade']
              preco = item['preco']
              st.write(f'{quantidade}x  {produto}: R$ {preco}')
              total_comanda += preco

          st.subheader(f'Total: {total_comanda}')