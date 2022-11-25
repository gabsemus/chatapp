import streamlit as st
from datetime import datetime
from pytz import timezone
import random

def data_hora():
   data_hora = datetime.now()
   fuso_horario = timezone('America/Sao_Paulo')
   data_hora = data_hora.astimezone(fuso_horario)
   data = data_hora.strftime('%d')
   # hora = data_hora.strftime('%H:%M')
   return data

def home():
    nome_local = 'Kingdom'
    st.title(f'Bem-vindo a {nome_local}')

    st.subheader(f"Hoje, dia {data_hora()}, temos as seguintes atrações: ")

    line = ['DJ Sande', 'DJ Stizi', 'DJ Aron Kawillian', 'DJ Gouveia']

    emoji = [':full_moon:', ':new_moon_with_face:', ':full_moon_with_face:', ':headphones:', ':hatched_chick:',
             ':lips:', ':fire:']

    for dj in line:
        rand_idx = random.randrange(len(emoji))
        random_num = emoji[rand_idx]
        st.markdown(f'{str(random_num)} **{dj}**')

    st.subheader(f"Temos as seguintes promoções: ")

    promo = {
        'Bebida': 'Gin em dobro até as 21h',
        'Rosh': 'Rosh em dobro até as 24h'
    }
    col1, col2 = st.columns(2)

    for produto in promo:
        with col1:
            st.markdown(f'**{produto}**')
        with col2:
            st.markdown(f'{promo[produto]}')

    st.subheader(f" :fire: Informações da Casa: :fire: ")

    st.markdown(
        """
    <style>
    [data-testid="stMetricLabel"] {
        font-size: 25px;
    }
    [data-testid="stMetricValue"] {
        font-size: 50px;
    }
  
    </style>
  
    """,
        unsafe_allow_html=True,
    )
    st.metric(label="Lotação da Casa", value=4)