import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # Here a new dataframe is created with the name bigCountries based on the condition 1 or Condition 2.
    bigCountries = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    # Returing the result with only showing the required columns of the dataframe.
    return bigCountries[['name', 'population', 'area']]


