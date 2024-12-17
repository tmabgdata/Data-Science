import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração inicial da página
st.set_page_config(page_title="Análise Exploratória de Dados", layout="wide")
st.title("Despesas empenhadas e relação com o PIB")

# Função para carregar os dados, usando cache para melhorar desempenho
@st.cache_data
def load_data():
    # Carrega os dados de um arquivo CSV e calcula a proporção entre valor empenhado e PIB
    data = pd.read_csv(r"D:\Repositories\Data-Science\AI_EDA\data\data.csv", sep=";")
    data['PROPORCAO'] = data['VALOREMPENHO'] / data['PIB']
    return data

# Carrega os dados
data = load_data()

# Configurações na barra lateral
with st.sidebar:
    st.header("Configurações")
    # Input para selecionar o número de entradas a serem exibidas
    top_n = st.number_input("Selecione o número de entradas para exibir", 
                            min_value=1, max_value=len(data), value=10)

# Cria abas para organização do conteúdo
tab1, tab2, tab3 = st.tabs(["Visão Geral", "Análise Detalhada", "Maiores Valores"])

# Aba 1: Visão geral dos dados
with tab1:
    st.header("Resumo dos Dados")
    st.write(data.describe())

# Aba 2: Análise detalhada dos dados
with tab2:
    st.header("Distribuição dos Dados")
    # Cria duas colunas para exibição de gráficos
    col1, col2 = st.columns(2)

    with col1:
        # Histograma do valor empenhado
        fig1 = px.histogram(data, x='VALOREMPENHO', 
                            title="Histograma do Valor Empenhado")
        st.plotly_chart(fig1, use_container_width=True)

        # Boxplot do valor empenhado
        fig2 = px.box(data, x='VALOREMPENHO', 
                      title="Boxplot do Valor Empenhado")
        st.plotly_chart(fig2, use_container_width=True)

    with col2:
        # Histograma do PIB
        fig3 = px.histogram(data, x='PIB', 
                            title="Histograma do PIB")
        st.plotly_chart(fig3, use_container_width=True)

        # Boxplot do PIB
        fig4 = px.box(data, x='PIB', 
                      title="Boxplot do PIB")
        st.plotly_chart(fig4, use_container_width=True)

# Aba 3: Maiores valores
with tab3:
    st.header("Maiores Valores")
    # Cria três colunas para exibição de gráficos
    col1, col2, col3 = st.columns(3)

    with col1:
        # Maiores valores empenhados
        hg_commit = data.nlargest(top_n, 'VALOREMPENHO')
        fig = px.bar(hg_commit, x='MUNICIPIO', y='VALOREMPENHO', 
                     title="Maiores Valores Empenhados")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # Maiores PIBs
        hg_pibs = data.nlargest(top_n, 'PIB')
        fig2 = px.bar(hg_pibs, x='MUNICIPIO', y='PIB', 
                      title="Maiores PIBs")
        st.plotly_chart(fig2, use_container_width=True)

    with col3:
        # Maiores proporções entre valor empenhado e PIB
        hg_prop = data.nlargest(top_n, 'PROPORCAO')
        fig3 = px.pie(hg_prop, values='PROPORCAO', names='MUNICIPIO', 
                      title="Maiores Proporções de Empenho em Relação ao PIB")
        st.plotly_chart(fig3, use_container_width=True)
