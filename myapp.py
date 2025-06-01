from dash import Dash, dcc, html, Input, Output 
import plotly.express as px 
import plotly.data as pldata 

df = pldata.gapminder(return_type='pandas') 

countries = df['country'].unique()
# Initialize Dash app
app = Dash(__name__)
server = app.server 

# Layout This section creates the HTML components
app.layout = html.Div([# This div is for the dropdown you see at the top, and also for the graph itself
    dcc.Dropdown(# This creates the dropdown
        id="country-dropdown",
        options=[{"label": country, "value": country} for country in countries],
        value="Canada" # This is the initial value
    ),
    dcc.Graph(id="gdp-growth") 
])

# Callback for dynamic updates
@app.callback(# This decorator is decorating the update_graph() function.
    # Because of the decorator, the update_graph() will be called when the country-dropdown changes, passing the value selected in the dropdown.
    Output("gdp-growth", "figure"), # get the graph back
    [Input("country-dropdown", "value")]  # When you pass in the value of the dropdown.
)
def update_graph(selected_country):  # This function is what actually does the plot, by calling Plotly, in this case a line chart of gdp (which is the index) vs. the chosen country.
    filtered_df = df[df['country'] == selected_country]
    fig = px.line(
        filtered_df,
        x="year",
        y="gdpPercap",
        title=f"GDP per capita for {selected_country}"
    )
    return fig

# Run the app
if __name__ == "__main__": # if this is the main module of the program, and not something included by a different module
    app.run(debug=True) # start the Flask web server