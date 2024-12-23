import pandas_profiling as pp
from utils import fetch_data_from_db
from const import sql_query

# Caminho do arquivo de configuração e saída
config_path = r'D:\Repositories\Data-Science\Credit_Score_Novadrive\EDA\config.yaml'
output_csv_path = r'D:\Repositories\Data-Science\Credit_Score_Novadrive\data\raw_data\data.csv'

# Obtendo os dados do banco e salvando o CSV
df_resultado = fetch_data_from_db(sql_query, config_path, output_csv_path)

# Gerando o relatório Pandas Profiling
if not df_resultado.empty:
    profile = pp.ProfileReport(df_resultado)
    profile.to_file(
        output_file=r'D:\Repositories\Data-Science\Credit_Score_Novadrive\EDA\eda_reports\pandas_profiling_report.html'
    )
else:
    print("Nenhum dado foi retornado para análise com Pandas Profiling.")
