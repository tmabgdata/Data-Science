import os
import pandas as pd
import yaml
import psycopg2
import logging

# Configuração do logger
logging.basicConfig(level=logging.ERROR)

def fetch_data_from_db(sql_query, config_path, output_csv_path=None):
    try:
        # Verificar se o arquivo de configuração existe
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Arquivo de configuração não encontrado: {config_path}")

        # Lendo o arquivo de configuração
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)

        # Conexão com o banco de dados
        with psycopg2.connect(
            dbname=config['database_config']['dbname'], 
            user=config['database_config']['user'], 
            password=config['database_config']['password'], 
            host=config['database_config']['host']
        ) as con:
            with con.cursor() as cursor:
                cursor.execute(sql_query)

                # Obtendo os dados e criando o DataFrame
                data = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]
                df = pd.DataFrame(data, columns=columns)
                
                # Verificação e salvando o DataFrame como CSV
                if df.empty:
                    logging.warning("A consulta retornou nenhum dado.")
                else:
                    print(f"Quantidade de linhas e colunas: {df.shape}")
                    
                    # Salvando o CSV se o caminho for fornecido
                    if output_csv_path:
                        # Cria os diretórios necessários, se não existirem
                        os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)
                        df.to_csv(output_csv_path, index=False, encoding='utf-8')
                        print(f"Dados salvos em: {output_csv_path}")
                        
    except psycopg2.Error as e:
        logging.error(f"Erro ao conectar ou executar a consulta no banco de dados: {e}")
        df = pd.DataFrame()  # Retorna um DataFrame vazio em caso de erro
    except Exception as e:
        logging.error(f"Erro inesperado: {e}")
        df = pd.DataFrame()  # Retorna um DataFrame vazio em caso de erro

    return df
