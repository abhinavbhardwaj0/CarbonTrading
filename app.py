import numpy as np
import pandas as pd
import spacy
import matplotlib.pyplot as plt
import plotly
import plotly.graph_objs as go
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas_datareader
from pandas_datareader import data as web
from datetime import datetime as dt
import plotly.express as px
import dash_daq as daq
from get_extrapolate import extrapolate, countries_list, sectors_list

app = dash.Dash('Hello World')

app.layout = html.Div([
    html.Div([
        html.Div([
            html.Label('Country'),
            dcc.Dropdown(
                id='country',
                options= countries_list,
                multi=False,
                value='Germany'
            ),
        ]),
        html.Div([
            html.Label('Sector'),
            dcc.Dropdown(
                id='sector',
                options=sectors_list,
                multi=False,
                value= 'bulk chemicals'
            ),
        ]),
        html.Div([html.Label('Annual Freely Allocated Allowance Percent Reduction (from 2021)'),
    daq.Knob(id='percent', max=30, value = 5),
    html.Div(id='knob-output-1')
]),
    ]),
    dcc.Graph(id='my-graph')
])

@app.callback(Output('my-graph', 'figure'), [Input('country', 'value'), Input('sector', 'value'), Input('percent', 'value')])
def update_graph(selected_dropdown_value1, selected_dropdown_value2, value3): #1, selected_dropdown_value2):
    
    country, sector, percent = selected_dropdown_value1, selected_dropdown_value2, float(value3)
    x1,x2,y1,y2 = extrapolate(country, sector, percent)
    x = x1 + x2
    y = y1 + y2
    feature = ['Historical']*(len(x1)) + ['Projected']*(len(x2))
    years = list(range(2005, 2031))
    df = pd.DataFrame({'x': x, 'y': y, 'DataType': feature, 'year': years})

    data = px.bar(
        df, x='year', y='y', 
        color="DataType",
        color_discrete_sequence=px.colors.qualitative.Set1,
        hover_data = ['year', 'x', 'y'],
        title= country.upper() +': Annual Emissions<br><sup>Sector: ' + sector.upper() + '</sup>',
        labels={
                     "x": "Total Allocated Allowances (tonnes of CO2)",
                     "y": "Emissions (tonnes of CO2)",
                     "DataType": " "
                 }
    )

    return data

app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

if __name__ == '__main__':
    app.run_server()