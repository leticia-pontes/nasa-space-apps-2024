import os
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, callback, Output, Input
from dash import dash_table

# Path to the local CSV file
csv_file = 'assets/downloaded_file.csv'

def load_csv():
    return pd.read_csv(csv_file)

# Function to get the last modified time of the file
def get_last_modified_time(filepath):
    return os.path.getmtime(filepath)

# Initialize the Dash app
app = Dash(__name__)

# Load initial data
df = load_csv()
last_modified = get_last_modified_time(csv_file)

# Define the app layout
app.layout = [
    html.H1(children='Title of Dash App', style={'textAlign': 'center'}),
    dcc.Dropdown(df['country'].unique(), 'Brazil', id='dropdown-selection'),
    html.Br(),
    dcc.Input(
        id='year-input',
        type='number',
        placeholder='Enter Year',
        style={'marginBottom': '20px', 'width': '10%'},
        min=1900,  # Set a minimum year
        step=1,    # Set step to 1 to ensure whole numbers only
        value=None,
        inputMode='numeric',  # This ensures the numeric keyboard on mobile
        debounce=True,  # Optional: Delay input processing to avoid rapid updates
    ),
    html.Button('Submit', id='submit-button', n_clicks=0, style={'marginRight': '10px', 'marginLeft': '10px'}),
    html.Button('Clear', id='clear-button', n_clicks=0),
    
    # Add margins around the graph
    dcc.Graph(id='graph-content'),
    html.Br(), html.Br(),
    
    dash_table.DataTable(
        id='data-table',
        columns=[],
        data=[],
        page_size=10,
        style_table={'margin': '20px'},  # Add margin to the table
        style_cell={
            'padding': '10px',    # Add padding to cells
            'border': '1px solid #d9d9d9',  # Add border to cells
        },
        style_header={
            'backgroundColor': '#f1f1f1',  # Background color for header
            'fontWeight': 'bold',           # Bold header text
            'textAlign': 'center',          # Center align header text
            'border': '1px solid #d9d9d9',  # Border for header
        },
        style_data={
            'whiteSpace': 'normal',         # Allow text wrapping
            'height': 'auto',               # Allow dynamic height
        },
        style_data_conditional=[
            {
                'if': {'column_id': 'country'},  # Specific column for country
                'textAlign': 'left'              # Align text to the left
            },
            {
                'if': {'column_id': 'year'},     # Specific column for year
                'textAlign': 'center'            # Center align text
            },
            {
                'if': {'column_id': 'pop'},      # Specific column for population
                'textAlign': 'right'             # Align text to the right
            },
        ]
    )
]

@app.callback(
    [Output('graph-content', 'figure'),  # Output for the graph
     Output('data-table', 'data'),  # Output for table data
     Output('data-table', 'columns'),  # Output for table columns
     Output('year-input', 'value')],  # Clear input field
    [Input('dropdown-selection', 'value'),
     Input('year-input', 'value'),
     Input('submit-button', 'n_clicks'),
     Input('clear-button', 'n_clicks')]
)
def update_output(selected_country, input_year, submit_clicks, clear_clicks):
    global df, last_modified

    # Check if the file was modified
    current_modified = get_last_modified_time(csv_file)

    if current_modified != last_modified:
        # Reload the CSV if it was modified
        df = load_csv()
        last_modified = current_modified

    # Handle Clear button click
    if clear_clicks > 0:
        return {}, [], [], None  # Clear graph, table, and input

    # Handle Submit button click
    if submit_clicks > 0 and input_year is not None:
        dff = df[(df['country'] == selected_country) & (df['year'] == int(input_year))]

        # Check if the filtered DataFrame is empty
        if not dff.empty:
            # Define columns for the table
            columns = [{"name": col, "id": col} for col in ['country', 'year', 'pop']]
            return None, dff.to_dict('records'), columns, None  # Hide graph and show table

    # If no valid input year or submit clicks, show the graph
    dff = df[df['country'] == selected_country]
    fig = px.bar(dff, x='year', y='pop', title=f'Population over Years for {selected_country}')

    # Add margin to the figure
    fig.update_layout(margin=dict(l=200, r=200, t=80, b=100))

    return fig, [], [], input_year  # Show graph when no valid table data

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
