import pandas as pd
from datetime import datetime
import numpy as np
import random as python_random
import joblib
import os

from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import RFE
import tensorflow as tf

# Importando funções auxiliares e configurações
from utils import *  # Certifique-se de que o arquivo utils.py esteja presente na pasta correta
import const  # Este arquivo contém a variável consulta_sql

# Reprodutibilidade
seed = 41
np.random.seed(seed)
python_random.seed(seed)
tf.random.set_seed(seed)

# Caminho para salvar os dados limpos
output_dir = r'D:\Repositories\Data-Science\Credit_Score_Novadrive\data\cleaned_data'
os.makedirs(output_dir, exist_ok=True)

# Definir o caminho do arquivo CSV
output_csv_path = os.path.join(output_dir, 'cleaned_data.csv')

# Dados brutos - busque os dados usando a função fetch_data_from_db com a consulta definida no const.py
df = fetch_data_from_db(const.sql_query, config_path, output_csv_path)

# Verificando se os dados foram carregados corretamente
if df.empty:
    print("Nenhum dado foi carregado.")
else:
    print(f"Dados carregados com sucesso: {df.shape} linhas, {df.columns} colunas")

    # Conversão de tipo
    df['idade'] = df['idade'].astype(int)
    df['valorsolicitado'] = df['valorsolicitado'].astype(float)
    df['valortotalbem'] = df['valortotalbem'].astype(float)

    # Tratamento de Nulos
    df = substitui_nulos(df)

    # Trata Erros de Digitação - Ajuste conforme necessário
    profissoes_validas = ['Advogado', 'Arquiteto', 'Cientista de Dados', 'Contador', 'Dentista', 'Empresário',
                           'Engenheiro', 'Médico', 'Programador']
    df = corrigir_erros_digitacao(df, 'profissao', profissoes_validas)

    # Trata Outliers
    df = tratar_outliers(df, 'tempoprofissao', 0, 70)
    df = tratar_outliers(df, 'idade', 0, 110)

    # Feature Engineering
    df['proporcaosolicitadototal'] = df['valorsolicitado'] / df['valortotalbem']
    df['proporcaosolicitadototal'] = df['proporcaosolicitadototal'].astype(float)

    # Salvando o DataFrame limpo em CSV com o nome 'cleaned_data.csv'
    output_csv_path = os.path.join(output_dir, 'cleaned_data.csv')
    df.to_csv(output_csv_path, index=False, encoding='utf-8')
    print(f"Dados limpos salvos em: {output_csv_path}")

    # Dividindo Dados
    X = df.drop('classe', axis=1)
    y = df['classe']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=seed)

    # Normalização - Salvar os escaladores para os dados de treino e teste
    X_test = save_scalers(X_test, ['tempoprofissao', 'renda', 'idade', 'dependentes', 'valorsolicitado', 'valortotalbem', 'proporcaosolicitadototal'])
    X_train = save_scalers(X_train, ['tempoprofissao', 'renda', 'idade', 'dependentes', 'valorsolicitado', 'valortotalbem', 'proporcaosolicitadototal'])

    # Codificação - Mapear classes para valores numéricos
    mapeamento = {'ruim': 0, 'bom': 1}
    y_train = np.array([mapeamento[item] for item in y_train])
    y_test = np.array([mapeamento[item] for item in y_test])

    # Codificando variáveis categóricas
    X_train = save_encoders(X_train, ['profissao', 'tiporesidencia', 'escolaridade', 'score', 'estadocivil', 'produto'])
    X_test = save_encoders(X_test, ['profissao', 'tiporesidencia', 'escolaridade', 'score', 'estadocivil', 'produto'])

    # Seleção de Atributos com RFE (Recursive Feature Elimination)
    model = RandomForestClassifier()
    # Instancia o RFE
    selector = RFE(model, n_features_to_select=10, step=1)
    selector = selector.fit(X_train, y_train)
    # Transforma os dados
    X_train = selector.transform(X_train)
    X_test = selector.transform(X_test)

    # Salva o modelo do RFE
    joblib.dump(selector, r'D:\Repositories\Data-Science\Credit_Score_Novadrive\Data_Analysis_Cleaning\objects\selector.joblib')
    print("Modelo de seleção de atributos (RFE) salvo com sucesso.")
