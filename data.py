import pandas as pd


def get_pop_data(population_src_file, locations_src_file, debug=False):
    population_src = pd.read_csv(population_src_file)
    population = population_src[population_src.Variant == "Medium"][
        ["LocID", "Location", "Time", "PopTotal", "PopMale", "PopFemale"]
    ]

    locations_src = pd.read_excel(locations_src_file, sheet_name="DB")
    locations = locations_src[locations_src.LocType == 4][
        ["LocID", "SubRegName", "GeoRegName"]
    ]

    if debug:
        print("--- population dataframe ---")
        print(population.info())
        print(population.head())
        print(population.tail())
        print("--- locations dataframe ---")
        print(locations.info())
        print(locations.head())
        print(locations.tail())

    pop_data = population.merge(locations)
    pop_data.drop(columns="LocID", inplace=True)
    pop_data = pd.melt(
        pop_data,
        id_vars=["Time", "GeoRegName", "SubRegName", "Location"],
        value_vars=["PopMale", "PopFemale"],
        var_name="PopType",
        value_name="Population",
    )
    pop_data["Population"] = pop_data["Population"] * 1000

    if debug:
        print("--- pop_data dataframe ---")
        print(pop_data.info())
        print(pop_data.head())
        print(pop_data.tail())

    columns_list = list([pop_data.columns.tolist()])
    values_list = pop_data.values.tolist()
    pop_data = columns_list + values_list

    return pop_data