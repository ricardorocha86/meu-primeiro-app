import streamlit as st

st.title('Meu primeiro App ❤')

st.header('Vamos fazer algo com interatividade!')

n = st.number_input('Entre com um numero')

st.write(f'O número que você escolheu ao quadrado é {n**2}')
