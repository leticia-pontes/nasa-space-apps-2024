import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

data = {
    'latitude': [37.7749, 34.0522],
    'longitude': [-122.4194, -118.2437],
    'city': ['San Francisco', 'Los Angeles'],
    'population': [883305, 3990456]
}
df = pd.DataFrame(data)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Mapa Interativo'),
    dcc.Dropdown(
        id='city-filter',
        options=[{'label': city, 'value': city} for city in df['city']],
        multi=True,
        placeholder='Selecione as cidades'
    ),
    dcc.Graph(id='map', style={'height': '70vh', 'width': '70%', 'margin':'auto'})
])

@app.callback(
    Output('map', 'figure'),
    Input('city-filter', 'value')
)
def update_map(selected_cities):
    if not selected_cities:
        filtered_df = df
    else:
        filtered_df = df[df['city'].isin(selected_cities)]
    
    fig = px.scatter_mapbox(
        filtered_df,
        lat='latitude',
        lon='longitude',
        hover_name='city',
        size='population',
        size_max=15,
        zoom=4,
        title='População das Cidades Selecionadas'
    )
    fig.update_layout(mapbox_style="open-street-map")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
