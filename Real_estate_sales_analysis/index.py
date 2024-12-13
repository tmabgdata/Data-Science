from dash import html, dcc, Dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import os

from app import app
from _histogram import *
from _map import *
from _controllers import *

# ============================================
# DATA INGESTION
# ============================================

# Caminho relativo para o arquivo CSV
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, "data", "cleaned_data.csv")
df_data = pd.read_csv(data_path, index_col=0)

# Validação de colunas
required_columns = ["LATITUDE", "LONGITUDE", "GROSS SQUARE FEET", "YEAR BUILT", "SALE DATE", "SALE PRICE"]
if not all(col in df_data.columns for col in required_columns):
    raise ValueError(f"O arquivo CSV deve conter as colunas: {', '.join(required_columns)}")

# Pré-processamento dos dados
mean_lat = df_data["LATITUDE"].mean()
mean_long = df_data["LONGITUDE"].mean()

df_data["size_m2"] = df_data["GROSS SQUARE FEET"] / 10.764
df_data = df_data[df_data["YEAR BUILT"] > 0]
df_data["SALE DATE"] = pd.to_datetime(df_data["SALE DATE"])

# Ajustando valores atípicos
df_data.loc[df_data["size_m2"] > 10000, "size_m2"] = 10000  # Max built size = 10k
df_data.loc[df_data["SALE PRICE"] > 50000000, "SALE PRICE"] = 50000000  # Max price value = 50m
df_data.loc[df_data["SALE PRICE"] < 100000, "SALE PRICE"] = 100000  # Min price value = 100k

# ============================================
# LAYOUT
# ============================================

app.layout = dbc.Container(
    children=[
        dbc.Row([
            dbc.Col([controllers], md=3),
            dbc.Col([map, hist], md=9),
        ]),
        html.H1("Testando a Exibição dos Componentes")
    ],
    fluid=True
)


# ============================================
# EXECUÇÃO DO APP
# ============================================

if __name__ == "__main__":
    app.run_server(debug=True, port=8050, host='0.0.0.0')

