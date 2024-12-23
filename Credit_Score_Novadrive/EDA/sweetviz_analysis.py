import sweetviz as sv
from utils import fetch_data_from_db
from const import sql_query

# Caminho do arquivo de configuração e saída
config_path = r'D:\Repositories\Data-Science\Credit_Score_Novadrive\EDA\config.yaml'
output_csv_path = r'D:\Repositories\Data-Science\Credit_Score_Novadrive\data\raw_data\data.csv'

# Obtendo os dados do banco e salvando o CSV
df_resultado = fetch_data_from_db(sql_query, config_path, output_csv_path)

# Gerando o relatório Sweetviz
if not df_resultado.empty:
    sv_report = sv.analyze(df_resultado)
    sv_report.show_html(
        filepath=r'D:\Repositories\Data-Science\Credit_Score_Novadrive\EDA\eda_reports\sweetviz_report.html', 
        open_browser=True
    )
else:
    print("Nenhum dado foi retornado para análise com Sweetviz.")
