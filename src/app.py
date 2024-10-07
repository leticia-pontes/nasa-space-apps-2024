import dash
from dash import dcc, html, Input, Output
import plotly.express as px
from geocode import get_latitude_longitude  # Importando a função de geocode.py
from moisture import get_moisture
from earth_engine import initialize_earth_engine  # Importando a inicialização do Earth Engine

# Inicializa o Earth Engine
initialize_earth_engine()

# Inicializa a aplicação Dash
app = dash.Dash(__name__)

# Layout da aplicação
app.layout = html.Div([
    html.H1('Buscar Localização'),
    html.Div([
        html.Label('Digite o endereço:'),
        dcc.Input(id='address', type='text', required=True),
        html.Button('Buscar', id='search-button', n_clicks=0),
    ]),
    html.Div(id='output-address', style={'margin-top': '20px'}),
    html.Div(id='output-moisture', style={'margin-top': '20px'}),
    html.H1('Mapa Interativo'),
    dcc.Graph(id='map', style={'height': '70vh', 'width': '70%', 'margin': 'auto'})
])

# Callback para lidar com o botão de busca e atualizar o mapa
@app.callback(
    Output('output-address', 'children'),
    Output('output-moisture', 'children'),
    Output('map', 'figure'),
    Input('search-button', 'n_clicks'),
    Input('address', 'value')
)
def update_output(n_clicks, address):
    # Inicializa as coordenadas do endereço buscado
    latitude, longitude = None, None
    address_output = ''
    moisture_output = ''
    
    if n_clicks > 0 and address:
        latitude, longitude, city_name = get_latitude_longitude(address)
        address_output = f'Endereço buscado: {address}, Latitude: {latitude}, Longitude: {longitude}, Cidade: {city_name}'
        
        umidade = get_moisture(latitude, longitude)
        moisture_output = f'Nível de umidade do solo: {umidade}'

    # Criação do gráfico de dispersão
    fig = px.scatter_mapbox(
        lat=[latitude] if latitude is not None else [],
        lon=[longitude] if longitude is not None else [],
        hover_name=[address] if latitude is not None else [],
        size_max=15,
        zoom=17 if latitude is not None and longitude is not None else 4,
        title='Localização Buscada'
    )
    
    # Se o endereço foi buscado, adiciona um marcador para as coordenadas obtidas
    if latitude is not None and longitude is not None:
        fig.add_scattermapbox(
            lat=[latitude],
            lon=[longitude],
            mode='markers',
            marker=dict(size=10, color='red'),
            name='Localização Buscada'
        )
        
        # Focar no local buscado
        fig.update_layout(
            mapbox=dict(
                center=dict(lat=latitude, lon=longitude),
                zoom=18
            )
        )

    # Configuração do estilo do mapa
    fig.update_layout(mapbox_style="open-street-map")
    
    # Atualização das propriedades do marcador
    fig.update_traces(marker=dict(opacity=0.7, sizemode='diameter', size=10))
    
    return address_output, moisture_output, fig

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=5000, debug=True)
