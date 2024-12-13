import dash
import dash_bootstrap_components as dbc

# Configuração do Dash App
app = dash.Dash(__name__, 
                external_stylesheets=[dbc.themes.SLATE], 
                title="Real Estate Analysis")

# Servidor para uso com aplicações externas (e.g., Gunicorn)
server = app.server

# Configuração para servir scripts localmente (opcional)
app.scripts.config.serve_locally = True
