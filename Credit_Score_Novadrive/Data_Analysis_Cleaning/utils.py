import os
import pandas as pd
import yaml
import psycopg2
import logging
from fuzzywuzzy import process
from sklearn.preprocessing import StandardScaler, LabelEncoder
import joblib

# Configuração do logger
logging.basicConfig(level=logging.ERROR)

# Função para substituir valores nulos
def substitui_nulos(df):
    for coluna in df.columns:
        if df[coluna].dtype == 'object':
            moda = df[coluna].mode()[0]
            df[coluna].fillna(moda, inplace=True)
        else:
            mediana = df[coluna].median()
            df[coluna].fillna(mediana, inplace=True)
    return df

# Função para corrigir erros de digitação utilizando fuzzy matching
def corrigir_erros_digitacao(df, coluna, lista_valida):
    for i, valor in enumerate(df[coluna]):
        valor_str = str(valor) if pd.notnull(valor) else valor

        if valor_str not in lista_valida and pd.notnull(valor_str):
            correcao = process.extractOne(valor_str, lista_valida)[0]
            df.at[i, coluna] = correcao
    return df

# Função para tratar outliers em uma coluna
def tratar_outliers(df, coluna, minimo, maximo):
    mediana = df[(df[coluna] >= minimo) & (df[coluna] <= maximo)][coluna].median()
    df[coluna] = df[coluna].apply(lambda x: mediana if x < minimo or x > maximo else x)
    return df

# Função para salvar os escaladores
def save_scalers(df, nome_colunas):
    objects_dir = r"D:\Repositories\Data-Science\Credit_Score_Novadrive\Data_Analysis_Cleaning\objects"
    
    for nome_coluna in nome_colunas:
        scaler = StandardScaler()
        df[nome_coluna] = scaler.fit_transform(df[[nome_coluna]])
        
        # Ajustando o caminho para salvar no diretório correto
        scaler_path = os.path.join(objects_dir, f"scaler_{nome_coluna}.joblib")
        joblib.dump(scaler, scaler_path)

    return df

# Função para salvar os codificadores (encoders)
def save_encoders(df, nome_colunas):
    objects_dir = r"D:\Repositories\Data-Science\Credit_Score_Novadrive\Data_Analysis_Cleaning\objects"
    
    for nome_coluna in nome_colunas:
        label_encoder = LabelEncoder()
        df[nome_coluna] = label_encoder.fit_transform(df[nome_coluna])
        
        # Ajustando o caminho para salvar no diretório correto
        encoder_path = os.path.join(objects_dir, f"labelencoder_{nome_coluna}.joblib")
        joblib.dump(label_encoder, encoder_path)

    return df

# Função para buscar dados do banco de dados, ajustar tipos e salvar em CSV
def fetch_data_from_db(sql_query, config_path, output_csv_path=None):
    """
    Função para buscar dados do banco de dados, ajustar tipos e salvar em CSV.
    """
    try:
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Arquivo de configuração não encontrado: {config_path}")

        # Lê o arquivo de configuração
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)

        # Conecta ao banco de dados
        with psycopg2.connect(
            dbname=config['database_config']['dbname'], 
            user=config['database_config']['user'], 
            password=config['database_config']['password'], 
            host=config['database_config']['host']
        ) as con:
            with con.cursor() as cursor:
                # Executa a consulta SQL
                cursor.execute(sql_query)
                data = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]

                # Cria um DataFrame a partir dos dados retornados
                df = pd.DataFrame(data, columns=columns)

                # Verifica se o DataFrame não está vazio
                if df.empty:
                    logging.warning("A consulta retornou nenhum dado.")
                else:
                    # Retorna o DataFrame sem processamento
                    print(f"Quantidade de linhas e colunas: {df.shape}")

                    # Salva os dados em um arquivo CSV, se o caminho for fornecido
                    if output_csv_path:
                        os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)
                        df.to_csv(output_csv_path, index=False, encoding='utf-8')
                        print(f"Dados salvos em: {output_csv_path}")
                return df

    except psycopg2.Error as e:
        logging.error(f"Erro ao conectar ou executar a consulta no banco de dados: {e}")
        return pd.DataFrame()  # Retorna um DataFrame vazio em caso de erro
    except Exception as e:
        logging.error(f"Erro inesperado: {e}")
        return pd.DataFrame()  # Retorna um DataFrame vazio em caso de erro

# Lendo a consulta SQL do arquivo
sql_query = ""
with open(r"D:\Repositories\Data-Science\Credit_Score_Novadrive\queries\data_denormalization.sql", "r", encoding="utf-8") as file:
    sql_query = file.read()

# Caminho do arquivo de configuração
config_path = r'D:\Repositories\Data-Science\Credit_Score_Novadrive\Data_Analysis_Cleaning\config.yaml'

# Buscando os dados do banco de dados
df = fetch_data_from_db(sql_query, config_path)
