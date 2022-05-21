# import library
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
from matplotlib import pyplot as plt
from pandas.plotting import register_matplotlib_converters
from dash.dependencies import Input,Output
import dash
from dash import Dash, html, dcc
from widgets import get_map, get_slider_map, get_bar_chart, get_donuts_chart, line_plot_conso, line_plot_tweet
from processing import get_top_df, get_population_distribution, get_rural_urban_distribution
import dash_bootstrap_components as dbc
from layout import display_filters, display_navbar, display_map_and_population, display_donuts, display_lines_plots

register_matplotlib_converters()

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# import data and clean data (importing csv into pandas)
conso = pd.read_csv("clean-data/clean_energy_consumption.csv", sep=",")
tw = pd.read_csv("clean-data/twitter_2022-05-21.csv", sep=";")

app.layout = html.Div(
    [
        display_navbar(),
        display_filters(conso),        
        display_map_and_population(conso),
        display_donuts(conso),
        display_lines_plots(conso, tw)
    ]
)        
       

def get_choosen_top_country(chosen_item):
    return int(chosen_item.split(" ")[1])

@app.callback(Output("country_population", "figure"),
              [Input("select-year", "value"), Input("select-top-country", "value")])
def update(year, top_country_input):
    filtered_df = conso[conso["Year"] == year]
    top_country = get_choosen_top_country(top_country_input)
    filtered_df = get_top_df(filtered_df, top_country)
    return get_bar_chart(filtered_df, "CountryName", "total_population",
        "Distribution of the population and avg energy consumption")

@app.callback(Output("age_distribution", "figure"),
              [Input("select-year", "value"), Input("select-top-country", "value")])
def update(year, top_country_input):
    filtered_df = conso[conso["Year"] == year]
    top_country = get_choosen_top_country(top_country_input)
    filtered_df = get_top_df(filtered_df, top_country)
    return get_donuts_chart(get_population_distribution(filtered_df), ["<15", "15>64", ">64"],
        "Age distribution")

@app.callback(Output("rural_urban", "figure"),
              [Input("select-year", "value"), Input("select-top-country", "value")])
def update(year, top_country_input):
    filtered_df = conso[conso["Year"] == year]
    top_country = get_choosen_top_country(top_country_input)
    filtered_df = get_top_df(filtered_df, top_country)
    return get_donuts_chart(get_rural_urban_distribution(filtered_df), ["Rural", "Urban"],
        "Rural vs Urban")

@app.callback(Output("elec_conso_capita", "figure"),
              [Input("select-top-country", "value")])
def update_country_population(top_country_input):
    top_country = get_choosen_top_country(top_country_input)
    filtered_df = get_top_df(conso, top_country)
    return line_plot_conso(filtered_df, "elect_consumption_Kwh_per_capita", 
        "electricity consumption per capita over the years")


app.run_server(debug=True)


