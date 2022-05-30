# import library

import dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash import html
from dash.dependencies import Input, Output
from pandas.plotting import register_matplotlib_converters

from layout import display_navbar, display_filters, display_map_and_population, display_donuts, display_lines_plots
from processing import get_top_df, get_population_distribution, get_rural_urban_distribution, \
    get_prod_energy_types_distribution
from widgets import scatter_plot, get_mix_chart, get_donuts_chart, line_plot_conso
from data_loader import get_twitter_files_path, merge_dataframes_from_path

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


def filter_by_date(df, date):
    return df[df["Year"] == date]


@app.callback(Output("country_population", "figure"),
              [Input("select-year", "value"), Input("select-top-country", "value")])
def update(year, top_country_input):
    filtered_df = filter_by_date(conso, year)
    top_country = get_choosen_top_country(top_country_input)
    filtered_df = get_top_df(filtered_df, top_country)
    return get_mix_chart(filtered_df, "CountryName",
                         "elect_consumption_Kwh_per_capita", "Electricity<br>consumption (Kwh)",
                         "total_population", "Population",
                         "Distribution of the population and avg energy consumption")


@app.callback(Output("age_distribution", "figure"),
              [Input("select-year", "value"), Input("select-top-country", "value")])
def update(year, top_country_input):
    filtered_df = filter_by_date(conso, year)
    top_country = get_choosen_top_country(top_country_input)
    filtered_df = get_top_df(filtered_df, top_country)
    return get_donuts_chart(get_population_distribution(filtered_df), ["<15", "15>64", ">64"],
                            "Age distribution")


@app.callback(Output("rural_urban", "figure"),
              [Input("select-year", "value"), Input("select-top-country", "value")])
def update(year, top_country_input):
    filtered_df = filter_by_date(conso, year)
    top_country = get_choosen_top_country(top_country_input)
    filtered_df = get_top_df(filtered_df, top_country)
    return get_donuts_chart(get_rural_urban_distribution(filtered_df), ["Rural", "Urban"],
                            "Rural vs Urban")


@app.callback(Output("energy_prod_type", "figure"),
              [Input("select-year", "value"), Input("select-top-country", "value")])
def update(year, top_country_input):
    filtered_df = filter_by_date(conso, year)
    top_country = get_choosen_top_country(top_country_input)
    filtered_df = get_top_df(filtered_df, top_country)
    return get_donuts_chart(get_prod_energy_types_distribution(filtered_df),
                            ["Hydroelectric", "Natural gas", "Nuclear", "Oil|Gas|Coal", "Renewable"],
                            "Types of energy production")


@app.callback(Output("elec_conso_capita", "figure"),
              [Input("select-multi-countries", "value")])
def update_country_population(selected_countries):
    if type(selected_countries) == str:
        selected_countries = [selected_countries]
    filtered_df = conso[conso["CountryName"].isin(selected_countries)]
    return line_plot_conso(filtered_df, "elect_consumption_Kwh_per_capita",
                           "electricity consumption per capita over the year")


@app.callback(Output("rural_vs_consumption", "figure"),
              [Input("select-multi-countries", "value")])
def update_country_population(selected_countries):
    if type(selected_countries) == str:
        selected_countries = [selected_countries]
    filtered_df = conso[conso["CountryName"].isin(selected_countries)]
    return scatter_plot(filtered_df, "rural_population_percent",
                        "elect_consumption_Kwh_per_capita")


app.run_server(debug=True)
