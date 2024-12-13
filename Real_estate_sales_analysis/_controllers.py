from dash import html, dcc
import dash_bootstrap_components as dbc
from app import app

list_of_locations = {
    "All": 0,
    "Manhattan": 1,
    "Bronx": 2,
    "Brooklyn": 3,
    "Queen": 4,
    "Staten Island": 5,  
}

slider_size = [100, 500, 1000, 10000, 10000000]

controllers = dbc.Row([
    html.Img(id="logo", src="/assets/icon.png", style={"width": "50%"}),
    html.H3("Real State Sales - NYC", style={"margin-top": "30px"}),
    html.P("1 Year Sales in New York Analysis"),
    
    html.H4("BOROUGH", style={"margin-top": "50px", "margin-bottom": "25px"}),
    dcc.Dropdown(
        id="location-dropdown",
        options=[{"label": i, "value": j} for i, j in list_of_locations.items()],
        value=0,
        placeholder="Select a borough",
        persistence=True
    ),
    
    html.Hr(style={"margin-top": "20px", "margin-bottom": "20px"}),

    html.H4("SIZE (M2)", style={"margin-top": "20px", "margin-bottom": "20px"}),
    dcc.Slider(
        min=0, max=4, id="slide-square-size",
        marks={i: str(j) for i, j in enumerate(slider_size)},
        value=0,
        persistence=True
    ),
    
    html.H4("Control Variable", style={"margin-bottom": "20px", "margin-top": "20px"})
])
