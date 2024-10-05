import os
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, callback, Output, Input
from dash import dash_table

# Path to the local CSV file
csv_file = 'assets/downloaded_file.csv'

def load_csv():
    """Load the CSV file into a DataFrame."""
    return pd.read_csv(csv_file)

def get_last_modified_time(filepath):
    """Get the last modified time of the file."""
    return os.path.getmtime(filepath)

# Initialize the Dash app
app = Dash(__name__)

# Load initial data
df = load_csv()
last_modified = get_last_modified_time(csv_file)

# Define the app layout
app.layout = html.Div([
    html.H1('Population by Year Graph', style={'textAlign': 'center'}),
    dcc.Dropdown(df['country'].unique(), 'Brazil', id='dropdown-selection'),
    html.Br(),
    dcc.Input(
        id='year-input',
        type='number',
        placeholder='Enter Year',
        style={'marginBottom': '20px', 'width': '10%'},
        min=1900,
        step=1,
        value=None,
        inputMode='numeric',
        debounce=True,
    ),
    html.Button('Submit', id='submit-button', n_clicks=0, style={'marginRight': '10px', 'marginLeft': '10px'}),
    html.Button('Clear', id='clear-button', n_clicks=0),
    html.Div(id='output-container'),  # Holds either the graph or the table based on the state
])

@app.callback(
    [Output('output-container', 'children'), Output('year-input', 'value')],
    [Input('dropdown-selection', 'value'),
     Input('year-input', 'value'),
     Input('submit-button', 'n_clicks'),
     Input('clear-button', 'n_clicks')]
)

def update_output(selected_country, input_year, submit_clicks, clear_clicks):
    global df, last_modified

    # Reload CSV if modified
    current_modified = get_last_modified_time(csv_file)
    if current_modified != last_modified:
        df = load_csv()
        last_modified = current_modified

    # Handle Clear button click
    if clear_clicks > 0:
        return generate_population_graph(selected_country), None  # Clear input and show graph

    # Handle Submit button click
    if submit_clicks > 0 and input_year is not None:
        return handle_submit(selected_country, input_year)

    # Show default graph if no valid input
    return generate_population_graph(selected_country), input_year

def generate_population_graph(selected_country):
    """Generate a bar graph for the selected country."""
    dff = df[df['country'] == selected_country]
    fig = px.bar(dff, x='year', y='pop', title=f'Population over Years for {selected_country}')
    fig.update_layout(margin=dict(l=200, r=200, t=80, b=100))
    return dcc.Graph(id='graph-content', figure=fig)

def handle_submit(selected_country, input_year):
    """Handle the submission of the year input."""
    dff = df[(df['country'] == selected_country) & (df['year'] == int(input_year))]

    if not dff.empty:
        columns = [{"name": col, "id": col} for col in ['country', 'year', 'pop']]
        table = dash_table.DataTable(
            id='data-table',
            columns=columns,
            data=dff.to_dict('records'),
            page_size=10,
            style_table={'margin': '20px'},
            style_cell={'padding': '10px', 'border': '1px solid #d9d9d9'},
            style_header={
                'backgroundColor': '#f1f1f1',
                'fontWeight': 'bold',
                'textAlign': 'center',
                'border': '1px solid #d9d9d9',
            },
            style_data_conditional=[
                {'if': {'column_id': 'country'}, 'textAlign': 'left'},
                {'if': {'column_id': 'year'}, 'textAlign': 'center'},
                {'if': {'column_id': 'pop'}, 'textAlign': 'right'},
            ]
        )
        return table, None  # Show table and clear input

    return generate_population_graph(selected_country), input_year  # Show graph

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
