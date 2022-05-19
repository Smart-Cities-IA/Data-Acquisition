# import library
import plotly.offline as py
import plotly.graph_objs as go
from plotly.figure_factory import create_table
import plotly.express as px
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from pandas.plotting import register_matplotlib_converters
from dash.dependencies import Input,Output
import dash
from dash import Dash, html, dcc
plt.style.use('ggplot')

register_matplotlib_converters()

app = dash.Dash(__name__)

# import data and clean data (importing csv into pandas)
df = pd.read_csv("clean-data/DataSmartCity.csv", sep=',')
#tw = pd.read_csv("clean-dat/twitter_2022.csv", sep=';')

# Managing of missing values
df.dropna(subset=['elec_energy_prod_hydroelectric_percent'], how='any', inplace=True)
df.dropna(subset=['elect_access_percent_population'], how='any', inplace=True)
df.dropna(subset=['population_largest_city'], how='any', inplace=True)

countries = df["CountryName"].unique()
# Partie energie electrique

cols_to_clean = list(df.columns)
cols_to_clean = cols_to_clean[4:]

for col_name in cols_to_clean:
  df[col_name + "_median_value"] = df.groupby(["CountryName"])[col_name].transform("median")
  df[col_name].fillna(df[col_name + "_median_value"], inplace=True)
df


col_options = [dict(label=x, value=x)
               for x in df['Year'].unique()]


# App layout
app.layout = html.Div(children=[
    html.H1("test"),
    dcc.Dropdown(id='Year', value='CHOOSE A YEAR', options=col_options),
    #dcc.Dropdown(id='List', value='CHOOSE A OPTION', options=col_options2)
    dcc.Graph(id="graph", figure={}),
    dcc.Graph(id="graph2", figure={})

])

@app.callback(Output('graph', 'figure'),
              [Input('Year', 'value')])
def cb(Year):
    Year = Year if Year else 1990
    df_year = df.query("Year == @Year")
    return px.bar(df_year, x="CountryName", y="elec_energy_prod_hydroelectric_percent"
                      )

@app.callback(Output('graph2', 'figure'),
              [Input('Year', 'value')])
def cb(Year):
    Year = Year if Year else 1990
    df_year = df.query("Year == @Year")
    return px.scatter(df_year,y="population_15_64_percent", x="elect_access_percent_population")

app.run_server(debug=True)


