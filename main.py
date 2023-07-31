import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpld3
import streamlit.components.v1 as components
import datetime


# ----------------------- CONFIGURAÇÕES INICIAIS -----------------
data = pd.read_table("database.tsv")
data.columns = ["Datai", "Dataf", "Regiao", "Estado", "Produto", "Npostospesquisados", "Unmedida", "Medr", "Desvr", "Minr", "Maxr", "Margr", "Coefr", "Medd", "Desvd", "Mind", "Maxd", "Coefd"]
st.header("Preços de Gasolina no Brasil")

dictNames = {"Datai":"DATA INICIAL", "Dataf":"DATA FINAL", "Regiao":"REGIAO", "Estado": "ESTADO",
             "Produto":"PRODUTO", "Npostospesquisados":"POSTOS PESQUISADOS", "Unmedida":"UN. MEDIDA",
             "Medr":"MEDIA REVENDA", "Desvr":"DESVIO PADRAO REVENDA", "Minr":"MINIMO REVENDA",
             "Maxr":"MAXIMO REVENDA", "Margr":"MARGEM REVENDA", "Coefr":"COEFICIENTE REVENDA",
             "Medd":"MEDIA DISTRIBUICAO", "Desvd":"DESVIO DISTRIBUICAO", "Mind":"MINIMO DISTRIBUICAO",
             "Maxd":"MAXIMO DISTRIBUICAO", "Coefd":"COEFICIENTE DISTRIBUICAO"}

# ----------------------------------------------------------------

# --------------------------- SIDEBAR ----------------------------
st.sidebar.title("Selecione os tipos de filtro")
col1Side, col2Side = st.sidebar.columns(2, gap="medium")
filtroRegiao = col1Side.checkbox("Região")
filtroEstado = col2Side.checkbox("Estado")

tipoVenda = st.sidebar.selectbox(
    'Selecione',
    ('Revenda', 'Distribuição'))

dataInicio = st.sidebar.date_input(
 "Data Início",
 datetime.date(2005, 1, 1))

dataFim = st.sidebar.date_input(
 "Data Fim",
 datetime.date(2021, 1, 1))

dataInicio = str(dataInicio)
dataFim = str(dataFim)

if filtroEstado:
    estados = st.sidebar.selectbox(
    "Estado",
    ("SAO PAULO", "RIO DE JANEIRO", "PARAIBA", "RIO GRANDE DO SUL", "BAHIA", "SANTA CATARINA", "RIO GRANDE DO NORTE", "MINAS GERAIS", "ESPIRITO SANTO", "PERNAMBUCO", "CEARA", "PARANA", "ALAGOAS", "SERGIPE", "MATO GROSSO DO SUL", "MATO GROSSO", "AMAZONAS", "GOIAS", "PIAUI", "MARANHAO", "DISTRITO FEDERAL", "PARA", "TOCANTINS", "RONDONIA", "ACRE", "RORAIMA", "AMAPA"))

if filtroRegiao:
    regioes = st.sidebar.selectbox(
        "Região",
        ("SUDESTE", "NORDESTE", "NORTE", "CENTRO OESTE", "SUL"))
# ----------------------------------------------------------------

info = data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim)].sample(n=50)

# --------------------------- MAIN FRAME -------------------------
col1, col2 = st.columns(2, gap="large")

if filtroRegiao and filtroEstado:
    info = data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Estado == estados) & (data.Regiao == regioes)].sample(n=50)
  
elif filtroRegiao and not filtroEstado:
    info = data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Regiao == regioes)].sample(n=50)
elif filtroEstado and not filtroRegiao:
    info = data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Estado == estados)].sample(n=50)
else:
    info = data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim)].sample(n=50)


if tipoVenda == 'Revenda':
    col1.markdown("# Desvio Padrão")
    col1.line_chart(info, y="Desvr", x="Dataf", height=350, width=800)
    col2.markdown("# Coef de Variação")
    col2.line_chart(info, y="Coefr", x="Dataf", height=350, width=800)

    col1.markdown("# Preços Mínimos")
    col1.line_chart(info, y="Minr", x="Dataf", height=350, width=800)
    col2.markdown("# Preços Máximos")
    col2.line_chart(info, y="Maxr", x="Dataf", height=350, width=800)
    st.markdown("# Preços Médios")
    st.line_chart(info, y="Medr", x="Dataf", height=350, width=800)
    st.markdown("# Preços Médios Por Estado")
    st.bar_chart(info, y="Medr", x="Estado", height=350, width=800)
    st.markdown("# Margem média revenda")
    st.line_chart(info, y='Margr', x="Dataf", height=350, width=800)

elif tipoVenda == 'Distribuição':
    info = data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim)].sample(n=50)
    col1.markdown("# Desvio Padrão")
    col1.line_chart(info, y="Desvd", x="Dataf", height=350, width=800)
    col2.markdown("# Coef de Variação")
    col2.line_chart(info, y="Coefd", x="Dataf", height=350, width=800)

    col1.markdown("# Preços Mínimos")
    col1.line_chart(info, y="Mind", x="Dataf", height=350, width=800)
    col2.markdown("# Preços Máximos")
    col2.line_chart(info, y="Maxd", x="Dataf", height=350, width=800)
    st.markdown("# Preços Médios")
    st.line_chart(info, y="Medd", x="Dataf", height=350, width=800)

# ----------------------------------------------------------------