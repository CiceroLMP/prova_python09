import streamlit as st
import pandas as pd
import plotly.express as px
import os

df = pd.read_csv("H:\prova_python09\dados_transporte_bh.csv", sep=";")
df.columns = df.columns.str.strip()
df["LINHA"] = df["LINHA"].astype(str).str.strip()
df = df[~df["PC"].isin([0, 3])]
viagens = df.groupby("LINHA").size().reset_index(name="viagens")


st.sidebar.markdown("---")
pagina = st.sidebar.radio(
    "Selecione a Visualização:",
    ["Gráfico de Barras", "Gráfico de Tabela"]
)



if pagina == "Gráfico de Barras":
    st.title("Filtro de 10 linhas de Viagem em gráfico de barras")
    st.header("Dados pego de: https://dados.pbh.gov.br/")
    
    st.dataframe(use_container_width=True)

if pagina == "Gráfico de Tabela":
    st.title("Filtro de 10 linhas de Viagem em tabela")
    st.header("Dados pego de: https://dados.pbh.gov.br/")

    st.dataframe(use_container_width=True)