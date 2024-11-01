import streamlit as st
import os
import json
st.markdown("""
    <style>
        .title1 {
            text-align: center;
            margin-bottom: -5px; /* Ajusta el margen inferior para reducir el espacio */
            font-size: 25px
        }
        .title2 {
            text-align: center;
            margin-top: -15px; /* Ajusta el margen superior para reducir el espacio */
            font-size: 25px
        }
    </style>
    <h1 class="title1">🐞YO SOY MARIQUITA🐞</h1>
    <h2 class="title2">La frase de hoy</h2>
""", unsafe_allow_html=True)

# Asegúrate de que el archivo 'frases.json' esté en el mismo directorio que tu notebook

with open('frases.json', 'r', encoding='utf-8') as archivo:
    lista_frases = json.load(archivo)


numero = st.number_input('', min_value=0, max_value=len(lista_frases)-1, step=1, value=None)
if numero == None:
  st.write('Escribe un número')
else:
  st.write(f'Frase número {numero}')
  st.write(f'_**"{lista_frases[numero + 1]}"**_', )