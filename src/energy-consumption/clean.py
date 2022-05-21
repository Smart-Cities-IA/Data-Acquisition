# importation des bibliothèques 
import numpy as np 
import pandas as pd 

def clean_data(df):
    df.drop('elect_access_percent_population', axis=1, inplace=True)
    # Groupby count of number of year by country
    # All the countries should have the same number of year
    total_year_per_country = df[["CountryName", "Year"]].groupby("CountryName").count().rename(columns={'Year':'total_years'})
    # The countries having more than 24 years (rows) should be put in the keep
    drop_countries = list(total_year_per_country[total_year_per_country["total_years"] > 24].index)

    df_high_nan = df[["CountryName", "elec_energy_prod_hydroelectric_percent"]]
    missing_value_per_country = df_high_nan["elec_energy_prod_hydroelectric_percent"].isnull().groupby([df_high_nan["CountryName"]]).sum().to_frame().rename(columns={'elec_energy_prod_hydroelectric_percent':'total_missing_data'})
    missing_value_per_country["percent_unavailability"] = round(missing_value_per_country["total_missing_data"] / 24 * 100, 1)
    missing_value_per_country["percent_unavailability"].value_counts()

    # Put in the keep_countries list the countries having less than 40% of data unavailability
    drop_countries = drop_countries + list(missing_value_per_country[missing_value_per_country["percent_unavailability"] >= 40]["percent_unavailability"].index)

    # Keep only the countries having less than 40% of data unavailability
    df_countries_filtered = df[~df["CountryName"].isin(drop_countries)]

    print("Energy Consumption Data Availability after cleaning")
    print((df_countries_filtered.isna().sum(axis=0)/df.shape[0]*100))

    return df_countries_filtered

def clean_country_name(country_name):
    clean_name = country_name.split(",")[0]
    return clean_name
