'''
Visualização de Dados
Base de Dados: Gas Prices in Brazil - https://www.kaggle.com/datasets/matheusfreitag/gas-prices-in-brazil
Autor: Leonardo Pompeu
Data: 22/07/2023
'''

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpld3
import streamlit.components.v1 as components
import datetime

data = pd.read_table("2004-2021.tsv")

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

def amostragem_simples(dataSize):
    np.random.seed(42)
    # 150 amostras, de 0 a 1, com reposição, probilidades equivalentes
    amostra = np.random.choice(a = [0, 1], size=dataSize, replace=True, p=[0.9, 0.1])
    data_final = data.loc[amostra == 0]
    return data_final

#dataFinal = amostragem_simples(120823)
#print(data.head(10))
#print(data.info())
#print(data.describe())
data.columns = ["Datai", "Dataf", "Regiao", "Estado", "Produto", "Npostospesquisados", "Unmedida", "Medr", "Desvr", "Minr", "Maxr", "Margr", "Coefr", "Medd", "Desvd", "Mind", "Maxd", "Coefd"]
st.header("Preços de Gasolina no Brasil")
option = st.sidebar.selectbox(
    'Selecione',
    ('Revenda', 'Distribuição'))

col1, col2 = st.columns(2, gap="large")

dataInicio = st.sidebar.date_input(
 "Data Início",
 datetime.date(2005, 1, 1))

dataFim = st.sidebar.date_input(
 "Data Fim",
 datetime.date(2021, 1, 1))

dataInicio = str(dataInicio)
dataFim = str(dataFim)



opcaoFiltro = st.sidebar.checkbox("Filtrar por Região")
opcaoFiltro2 = st.sidebar.checkbox("Filtrar por Estado")

if opcaoFiltro and opcaoFiltro2:
    estados = st.sidebar.selectbox(
    "Estado",
    ("SAO PAULO", "RIO DE JANEIRO", "PARAIBA", "RIO GRANDE DO SUL", "BAHIA", "SANTA CATARINA", "RIO GRANDE DO NORTE", "MINAS GERAIS", "ESPIRITO SANTO", "PERNAMBUCO", "CEARA", "PARANA", "ALAGOAS", "SERGIPE", "MATO GROSSO DO SUL", "MATO GROSSO", "AMAZONAS", "GOIAS", "PIAUI", "MARANHAO", "DISTRITO FEDERAL", "PARA", "TOCANTINS", "RONDONIA", "ACRE", "RORAIMA", "AMAPA"))

    regioes = st.sidebar.selectbox(
        "Região",
        ("SUDESTE", "NORDESTE", "NORTE", "CENTRO OESTE", "SUL"))
    if option == 'Revenda':
        col1.markdown("# Desvio Padrão")
        col1.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Estado == estados) & (data.Regiao == regioes)].sample(n=50), y="Desvr", x="Dataf")
        col2.markdown("# Coef de Variação")
        col2.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Estado == estados) & (data.Regiao == regioes)].sample(n=50), y="Coefr", x="Dataf")
    
        col1.markdown("# Preços Mínimos")
        col1.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Estado == estados) & (data.Regiao == regioes)].sample(n=50), y="Minr", x="Dataf")
        col2.markdown("# Preços Máximos")
        col2.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Estado == estados) & (data.Regiao == regioes)].sample(n=50), y="Maxr", x="Dataf")
        st.markdown("# Preços Médios")
        st.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Estado == estados) & (data.Regiao == regioes)].sample(n=50), y="Medr", x="Dataf")
        st.markdown("# Preços Médios Por Estado")
        st.bar_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Estado == estados) & (data.Regiao == regioes)].sample(n=50), y="Medr", x="Estado")
        st.markdown("# Margem média revenda")
        st.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Estado == estados) & (data.Regiao == regioes)].sample(n=50), y='Margr', x="Dataf")
    
    elif option == 'Distribuição':
        col1.markdown("# Desvio Padrão")
        col1.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Estado == estados) & (data.Regiao == regioes)].sample(n=10), y="Desvd", x="Dataf")
        col2.markdown("# Coef de Variação")
        col2.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Estado == estados) & (data.Regiao == regioes)].sample(n=10), y="Coefd", x="Dataf")
    
        col1.markdown("# Preços Mínimos")
        col1.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Estado == estados) & (data.Regiao == regioes)].sample(n=10), y="Mind", x="Dataf")
        col2.markdown("# Preços Máximos")
        col2.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Estado == estados) & (data.Regiao == regioes)].sample(n=10), y="Maxd", x="Dataf")
        st.markdown("# Preços Médios")
        st.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Estado == estados) & (data.Regiao == regioes)].sample(n=10), y="Medd", x="Dataf")
elif opcaoFiltro and not opcaoFiltro2:
    regioes = st.sidebar.selectbox(
        "Região",
        ("SUDESTE", "NORDESTE", "NORTE", "CENTRO OESTE", "SUL"))
    if option == 'Revenda':
        col1.markdown("# Desvio Padrão")
        col1.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Regiao == regioes)].sample(n=50), y="Desvr", x="Dataf")
        col2.markdown("# Coef de Variação")
        col2.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Regiao == regioes)].sample(n=50), y="Coefr", x="Dataf")
    
        col1.markdown("# Preços Mínimos")
        col1.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Regiao == regioes)].sample(n=50), y="Minr", x="Dataf")
        col2.markdown("# Preços Máximos")
        col2.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Regiao == regioes)].sample(n=50), y="Maxr", x="Dataf")
        st.markdown("# Preços Médios")
        st.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Regiao == regioes)].sample(n=50), y="Medr", x="Dataf")
        st.markdown("# Preços Médios Por Estado")
        st.bar_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Regiao == regioes)].sample(n=50), y="Medr", x="Estado")
        st.markdown("# Margem média revenda")
        st.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Regiao == regioes)].sample(n=50), y='Margr', x="Dataf")
    
    elif option == 'Distribuição':
        col1.markdown("# Desvio Padrão")
        col1.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Regiao == regioes)].sample(n=10), y="Desvd", x="Dataf")
        col2.markdown("# Coef de Variação")
        col2.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Regiao == regioes)].sample(n=10), y="Coefd", x="Dataf")
    
        col1.markdown("# Preços Mínimos")
        col1.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Regiao == regioes)].sample(n=10), y="Mind", x="Dataf")
        col2.markdown("# Preços Máximos")
        col2.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Regiao == regioes)].sample(n=10), y="Maxd", x="Dataf")
        st.markdown("# Preços Médios")
        st.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Regiao == regioes)].sample(n=10), y="Medd", x="Dataf")
elif opcaoFiltro2 and not opcaoFiltro:
    estados = st.sidebar.selectbox(
        "Estado",
        ("SAO PAULO", "RIO DE JANEIRO", "PARAIBA", "RIO GRANDE DO SUL", "BAHIA", "SANTA CATARINA", "RIO GRANDE DO NORTE", "MINAS GERAIS", "ESPIRITO SANTO", "PERNAMBUCO", "CEARA", "PARANA", "ALAGOAS", "SERGIPE", "MATO GROSSO DO SUL", "MATO GROSSO", "AMAZONAS", "GOIAS", "PIAUI", "MARANHAO", "DISTRITO FEDERAL", "PARA", "TOCANTINS", "RONDONIA", "ACRE", "RORAIMA", "AMAPA"))
    if option == 'Revenda':
        col1.markdown("# Desvio Padrão")
        col1.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Estado == estados)].sample(n=50), y="Desvr", x="Dataf")
        col2.markdown("# Coef de Variação")
        col2.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Estado == estados)].sample(n=50), y="Coefr", x="Dataf")
    
        col1.markdown("# Preços Mínimos")
        col1.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Estado == estados)].sample(n=50), y="Minr", x="Dataf")
        col2.markdown("# Preços Máximos")
        col2.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Estado == estados)].sample(n=50), y="Maxr", x="Dataf")
        st.markdown("# Preços Médios")
        st.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Estado == estados)].sample(n=50), y="Medr", x="Dataf")
        st.markdown("# Preços Médios Por Estado")
        st.bar_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Estado == estados)].sample(n=50), y="Medr", x="Estado")
        st.markdown("# Margem média revenda")
        st.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Estado == estados)].sample(n=50), y='Margr', x="Dataf")
    
    elif option == 'Distribuição':
        col1.markdown("# Desvio Padrão")
        col1.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Estado == estados)].sample(n=10), y="Desvd", x="Dataf")
        col2.markdown("# Coef de Variação")
        col2.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Estado == estados)].sample(n=10), y="Coefd", x="Dataf")
    
        col1.markdown("# Preços Mínimos")
        col1.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Estado == estados)].sample(n=10), y="Mind", x="Dataf")
        col2.markdown("# Preços Máximos")
        col2.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Estado == estados)].sample(n=10), y="Maxd", x="Dataf")
        st.markdown("# Preços Médios")
        st.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim) & (data.Estado == estados)].sample(n=10), y="Medd", x="Dataf")
else:
    if option == 'Revenda':
        col1.markdown("# Desvio Padrão")
        col1.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim)].sample(n=50), y="Desvr", x="Dataf")
        col2.markdown("# Coef de Variação")
        col2.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim)].sample(n=50), y="Coefr", x="Dataf")
    
        col1.markdown("# Preços Mínimos")
        col1.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim)].sample(n=50), y="Minr", x="Dataf")
        col2.markdown("# Preços Máximos")
        col2.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim)].sample(n=50), y="Maxr", x="Dataf")
        st.markdown("# Preços Médios")
        st.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim)].sample(n=50), y="Medr", x="Dataf")
        st.markdown("# Preços Médios Por Estado")
        st.bar_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim)].sample(n=50), y="Medr", x="Estado")
        st.markdown("# Margem média revenda")
        st.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim)].sample(n=50), y='Margr', x="Dataf")
    
    elif option == 'Distribuição':
        col1.markdown("# Desvio Padrão")
        col1.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim)].sample(n=10), y="Desvd", x="Dataf")
        col2.markdown("# Coef de Variação")
        col2.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim)].sample(n=10), y="Coefd", x="Dataf")
    
        col1.markdown("# Preços Mínimos")
        col1.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim)].sample(n=10), y="Mind", x="Dataf")
        col2.markdown("# Preços Máximos")
        col2.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim)].sample(n=10), y="Maxd", x="Dataf")
        st.markdown("# Preços Médios")
        st.line_chart(data.loc[(data.Dataf >= dataInicio) & (data.Dataf <= dataFim)].sample(n=10), y="Medd", x="Dataf")