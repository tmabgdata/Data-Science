import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

import const
from utils import *

# Caminho do arquivo de configuração
config_path = r'D:\Repositories\Data-Science\Credit_Score_Novadrive\EDA\config.yaml'

# Buscando os dados - o dataframe já está ajustado no utils.py
df = fetch_data_from_db(const.sql_query, config_path)

# Caminho para salvar os relatórios
output_dir = r'D:\Repositories\Data-Science\Credit_Score_Novadrive\EDA\eda_reports'
os.makedirs(output_dir, exist_ok=True)

# Função para criar as pastas para cada variável e salvar os gráficos
def criar_pasta_e_salvar_grafico_e_resumo(coluna, figura, nome_arquivo, resumo=None):
    pasta_variavel = os.path.join(output_dir, coluna)
    os.makedirs(pasta_variavel, exist_ok=True)  # Cria a pasta para a variável, se não existir
    
    # Salva o gráfico na pasta da variável
    if nome_arquivo.endswith('.png'):
        caminho_arquivo = os.path.join(pasta_variavel, nome_arquivo)
        figura.savefig(caminho_arquivo)
        plt.close(figura)
    
    # Salva o resumo na mesma pasta, se existir
    if resumo is not None:
        resumo_arquivo = os.path.join(pasta_variavel, f'resumo_{coluna}.txt')
        with open(resumo_arquivo, 'w') as f:
            f.write(f'Resumo estatístico de {coluna}:\n')
            f.write(str(resumo))

# Função para ajustar gráficos de variáveis categóricas
def plotar_variaveis_categoricas(df, variaveis_categoricas):
    for coluna in variaveis_categoricas:
        plt.figure(figsize=(10, 6))
        ax = sns.countplot(data=df, x=coluna, hue=coluna, palette="viridis", legend=False)
        ax.bar_label(ax.containers[0])  # Adiciona as contagens nas barras
        plt.title(f'Distribuição de {coluna}')
        plt.ylabel('Contagem')
        plt.xlabel(coluna)
        plt.xticks(rotation=45)
        plt.tight_layout()
        criar_pasta_e_salvar_grafico_e_resumo(coluna, plt.gcf(), f'distribuicao_{coluna}.png')

# Função para ajustar gráficos de variáveis numéricas
def plotar_variaveis_numericas(df, variaveis_numericas):
    for coluna in variaveis_numericas:
        # Boxplot
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=df, x=coluna, color='lightblue')
        plt.title(f'Boxplot de {coluna}')
        plt.tight_layout()
        criar_pasta_e_salvar_grafico_e_resumo(coluna, plt.gcf(), f'boxplot_{coluna}.png')

        # Histograma
        plt.figure(figsize=(10, 6))
        df[coluna].hist(bins=20, color='lightgreen')
        plt.title(f'Histograma de {coluna}')
        plt.xlabel(coluna)
        plt.ylabel('Frequência')
        plt.tight_layout()
        criar_pasta_e_salvar_grafico_e_resumo(coluna, plt.gcf(), f'histograma_{coluna}.png')

        # Gráfico de densidade
        plt.figure(figsize=(10, 6))
        sns.kdeplot(df[coluna], fill=True, color="orange")
        plt.title(f'Gráfico de Densidade de {coluna}')
        plt.xlabel(coluna)
        plt.ylabel('Densidade')
        plt.tight_layout()
        criar_pasta_e_salvar_grafico_e_resumo(coluna, plt.gcf(), f'densidade_{coluna}.png')

        # Estatísticas descritivas
        resumo = df[coluna].describe()
        criar_pasta_e_salvar_grafico_e_resumo(coluna, None, f'resumo_{coluna}.txt', resumo)

# Análise de valores nulos
def analisar_valores_nulos(df):
    nulos_por_coluna = df.isnull().sum()
    with open(os.path.join(output_dir, 'valores_nulos.txt'), 'w') as f:
        f.write('Análise de valores nulos:\n')
        f.write(str(nulos_por_coluna))

# Definindo as variáveis
variaveis_categoricas = ['profissao', 'tiporesidencia', 'escolaridade', 'score', 'estadocivil', 'produto']
variaveis_numericas = ['tempoprofissao', 'renda', 'idade', 'dependentes', 'valorsolicitado', 'valortotalbem']

# Executando as funções
plotar_variaveis_categoricas(df, variaveis_categoricas)
plotar_variaveis_numericas(df, variaveis_numericas)
analisar_valores_nulos(df)
