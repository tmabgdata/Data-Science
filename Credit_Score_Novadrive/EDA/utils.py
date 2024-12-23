import os
import pandas as pd
import yaml
import psycopg2
import logging

# Configuração do logger
logging.basicConfig(level=logging.ERROR)

# Função para ajustar os tipos de dados das colunas
def ajustar_tipos_de_dados(df):
    """
    Função para ajustar os tipos de dados das colunas conforme os requisitos.
    """
    df['profissao'] = df['profissao'].astype(str)
    df['tempoprofissao'] = df['tempoprofissao'].fillna(0).astype(int)
    df['renda'] = df['renda'].astype(float)
    df['escolaridade'] = df['escolaridade'].astype(str)
    df['score'] = df['score'].astype(str)
    df['idade'] = df['idade'].fillna(0).astype(int)
    df['dependentes'] = df['dependentes'].fillna(0).astype(int)
    df['estadocivil'] = df['estadocivil'].astype(str)
    df['produto'] = df['produto'].astype(str)
    df['valorsolicitado'] = df['valorsolicitado'].astype(float)
    df['valortotalbem'] = df['valortotalbem'].astype(float)
    df['classe'] = df['classe'].astype(str)

    # Preencher valores nulos nas variáveis categóricas com 'Desconhecido'
    df = df.fillna({
        'profissao': 'Desconhecido',
        'escolaridade': 'Desconhecido',
        'score': 'Desconhecido',
        'estadocivil': 'Desconhecido',
        'produto': 'Desconhecido',
        'classe': 'Desconhecido'
    })

    return df

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
                    # Ajusta os tipos de dados
                    df = ajustar_tipos_de_dados(df)
                    print(f"Quantidade de linhas e colunas após ajuste: {df.shape}")

                    # Salva os dados ajustados em um arquivo CSV
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
