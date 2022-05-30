import dash_bootstrap_components as dbc
from dash import dcc

from processing import get_top_df, get_population_distribution, get_rural_urban_distribution, \
    get_prod_energy_types_distribution
from widgets import get_slider_map, scatter_plot, get_mix_chart, get_donuts_chart, line_plot_conso, line_plot_tweet


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
                id="energy_prod_type",
                figure=get_donuts_chart(get_prod_energy_types_distribution(conso),
                                        ["Hydroelectric", "Natural gas", "Nuclear", "Oil|Gas|Coal", "Renewable"],
                                        "Types of energy production")
            )
        )
    ]
    )


def display_lines_plots(conso, tw):
    all_countries = list(conso["CountryName"].unique())
    init_country = "France"
    init_conso = conso[conso["CountryName"] == init_country]
    return dbc.Row([
        dbc.Row(dcc.Dropdown(all_countries, init_country, id="select-multi-countries", multi=True)),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id="elec_conso_capita",
                    figure=line_plot_conso(get_top_df(conso, 10), "elect_consumption_Kwh_per_capita",
                                           "electricity consumption per capita over the years")
                )
            ),

            dbc.Col(
                dcc.Graph(
                    id="rural_vs_consumption",
                    figure=scatter_plot(get_top_df(conso, 10), "rural_population_percent",
                                        "elect_consumption_Kwh_per_capita")
                )
            ),
            dbc.Row(
                dbc.Col(
                    dcc.Graph(
                        id="tweet_counts",
                        figure=line_plot_tweet(tw, "Tweet counts")
                    )
                )
            )

        ]
        )
    ])


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


def display_map(conso):
    return dcc.Graph(
        id="map",
        figure=get_slider_map(conso, "elect_consumption_Kwh_per_capita",
                              "Evolution of electricity consumption per capita over the years")
    )


def display_population(conso):
    return dcc.Graph(
        id="country_population",
        figure=get_mix_chart(get_top_df(conso, 10), "CountryName",
                             "elect_consumption_Kwh_per_capita", "Electricity<br>consumption (Kwh)",
                             "total_population", "Population",
                             "Distribution of the population and avg energy consumption")
    )


def display_map_and_population(conso):
    return dbc.Row(
        [
            dbc.Col(
                display_map(conso)
            ),
            dbc.Col(
                display_population(conso)
            )
        ]
    )
