import streamlit as st
import pandas as pd
import requests

url = "https://valorant-api.com/v1/agents"

st.title("Busca de Agentes do Valorant")

agenteValorant = st.text_input("Busque um Agente")

if agenteValorant != "":

    try:
        resp = requests.get(url.format(agenteValorant = agenteValorant))
        data = pd.DataFrame([resp.json()])

        st.dataframe(data)

    except Exception as err:
        st.error("Entre com um Agente válido")