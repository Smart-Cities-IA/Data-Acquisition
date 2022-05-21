import dash_bootstrap_components as dbc
from dash import dcc
from widgets import get_map, get_slider_map, get_bar_chart, get_donuts_chart, line_plot_conso, line_plot_tweet
from processing import get_top_df, get_population_distribution, get_rural_urban_distribution

def display_donuts(conso):
    return dbc.Row([
                dbc.Col(
                        dcc.Graph(  
                            id="age_distribution",
                            figure=get_donuts_chart(get_population_distribution(conso), ["<15", "15>64", ">64"],
                                "Age distribution")
                        )
                ),
                dbc.Col(
                        dcc.Graph(  
                            id="rural_urban",
                            figure=get_donuts_chart(get_rural_urban_distribution(conso), ["Rural", "Urban"],
                                "Rural vs Urban")
                        )
                ),
                dbc.Col(
                        dcc.Graph(  
                            id="age_donuts_3", # need to change the IS
                            figure=get_donuts_chart(get_population_distribution(conso), ["<15", "15>64", ">64"],
                                "Rural vs Urban")
                        )
                )
            ]
        )

def display_lines_plots(conso, tw):
    return dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id="elec_conso_capita",
                    figure=line_plot_conso(get_top_df(conso, 10), "elect_consumption_Kwh_per_capita",
                        "electricity consumption per capita over the years")
                )
            ),
            dbc.Col(
                dcc.Graph(
                    id="tweet_counts",
                    figure=line_plot_tweet(tw, "Tweet counts")
                )
            )
        ]            
        )   

def display_navbar():
    return dbc.NavbarSimple(
            brand="Energy Consumption Dashboard",
            brand_href="#",
            color="primary",
            dark=True,
        )    

def display_filters(conso):
    all_years = list(conso["Year"].unique())
    all_countries = list(conso["CountryName"].unique())
    total_countries = len(all_countries)
    top_countries = ["Top 10", "Top 20", "Top 30", "Top " + str(total_countries)]
    return dbc.Row(
            [
                dbc.Col(
                    dcc.Dropdown(all_years, all_years[0], id="select-year")
                ),
                dbc.Col(
                    dcc.Dropdown(top_countries, top_countries[0], id="select-top-country")
                )
            ]
        )

def display_map_and_population(conso):
    return dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(
                        id="map",
                        figure=get_slider_map(conso, "elect_consumption_Kwh_per_capita",
                            "Evolution of electricity consumption per capita over the years")
                    )
                ),
                dbc.Col(
                    dcc.Graph(
                        id="country_population",
                        figure=get_bar_chart(get_top_df(conso, 10), "CountryName","total_population", 
                            "Distribution of the population and avg energy consumption")
                    )            
                )
            ]
        )