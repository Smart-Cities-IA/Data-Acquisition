
import pandas as pd

world_data = pd.read_csv("raw-data/Indicators.csv")

indicators_rename = {
    "Population, ages 0-14 (% of total)": "population_0_14_percent",
    "Population, ages 15-64 (% of total)": "population_15_64_percent",
    "Population ages 65 and above (% of total)": "population_65_plus_percent",
    "Population, female (% of total)": "female_population_percent",
    "Population, total": "total_population",
    "Rural population (% of total population)": "rural_population_percent",
    "Population in largest city": "population_largest_city",
    "GDP growth (annual %)": "gdp_growth_annual_percent",
    "Surface area (sq. km)": "surface_area",
    "Population density (people per sq. km of land area)": "population_density",
    "Electricity production from renewable sources, excluding hydroelectric (% of total)": "elec_energy_prod_renewable_percent",
    "Electricity production from oil, gas and coal sources (% of total)": "elec_energy_prod_oil_gas_coal_percent",
    "Electricity production from nuclear sources (% of total)": "elec_energy_prod_nuclear_percent",
    "Electricity production from natural gas sources (% of total)": "elec_energy_prod_naturalgas_percent",
    "Electricity production from hydroelectric sources (% of total)": "elec_energy_prod_hydroelectric_percent",
    "Electric power consumption (kWh per capita)": "elect_consumption_Kwh_per_capita",
    "Access to electricity (% of population)": "elect_access_percent_population"
}

countries_to_remove = [
    "High income: nonOECD",
    "High income: OECD",
    "OECD members",
    "Other small states",
    "Low income",
    "Lower middle income",
    "Low & middle income",
    "Middle East & North Africa (all income levels)",
    "Middle income",
    "Middle East & North Africa (developing only)",
    "Latin America & Caribbean (all income levels)",
    "Upper middle income",
    "World",
    "South Asia",
    "Sub-Saharan Africa (developing only)",
    "Sub-Saharan Africa (all income levels)",
    "Small states",
    "Least developed countries: UN classification",
    "Central Europe and the Baltics",
    "East Asia & Pacific (developing only)",
    "East Asia & Pacific (all income levels)",
    "Europe & Central Asia (all income levels)",
    "Arab World",
    "Europe & Central Asia (developing only)",
    "Heavily indebted poor countries (HIPC)",
    "Latin America & Caribbean (developing only)",
    "Fragile and conflict affected situations",
    "High income"
]

def clean_country_name(country_name):
    clean_name = country_name.split(",")[0]
    return clean_name

# We only keep the rows related to the indicators we're interested in
# Get the all the keys of the indicators_rename dictionary
indicators_keep = list(indicators_rename.keys())
indicators_filter = world_data["IndicatorName"].isin(indicators_keep)
world_consumption_kpi_filtered = world_data[indicators_filter]

date_filter = (world_consumption_kpi_filtered["Year"] > 1989) & (world_consumption_kpi_filtered["Year"] < 2014)
world_filtered = world_consumption_kpi_filtered[date_filter]

# Rename the indicators by creating a kpis column
world_filtered["kpis"] = world_filtered["IndicatorName"].apply(lambda name: indicators_rename[name])

# Pivot the table 
world_clean = world_filtered.pivot_table(values='Value', index=["CountryCode","CountryName", "Year"], columns='kpis')
world_clean = world_clean.reset_index()

# Get rid off the countries that are not real countries
keep_countries_filter = ~world_clean["CountryName"].isin(countries_to_remove)
world_clean = world_clean[keep_countries_filter]

world_clean["CountryName"] = world_clean["CountryName"].apply(lambda name: clean_country_name(name))

world_clean.to_csv("exports/energy_consumption.csv")