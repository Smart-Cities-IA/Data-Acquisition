
import pandas as pd
from conf import indicators_rename, countries_to_remove
from clean import clean_data, clean_country_name

# read energy consumption data
world_data = pd.read_csv("raw-data/Indicators.csv")

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

filtered_data = clean_data(world_clean)

filtered_data.to_csv("clean-data/clean_energy_consumption.csv", index=False)
