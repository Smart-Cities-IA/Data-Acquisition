def get_top_df(df, nb_rank):
    population_per_country = df.sort_values('Year', ascending=False).groupby('CountryName').head(1)
    population_per_country.sort_values("total_population", ascending=False, inplace=True)
    top_countries = list(population_per_country.head(nb_rank)["CountryName"])
    return df[df["CountryName"].isin(top_countries)]


def get_population_distribution(df):
    under14 = df["population_0_14_percent"].mean()
    under64 = df["population_15_64_percent"].mean()
    above64 = df["population_65_plus_percent"].mean()
    return under14, under64, above64


def get_rural_urban_distribution(df):
    rural = df["rural_population_percent"].mean()
    urban = 100 - rural
    return rural, urban


def get_prod_energy_types_distribution(df):
    hydroelectric = df["elec_energy_prod_hydroelectric_percent"].mean()
    naturalgas = df["elec_energy_prod_naturalgas_percent"].mean()
    nuclear = df["elec_energy_prod_nuclear_percent"].mean()
    coal = df["elec_energy_prod_oil_gas_coal_percent"].mean()
    renewable = df["elec_energy_prod_renewable_percent"].mean()
    return hydroelectric, naturalgas, nuclear, coal, renewable
