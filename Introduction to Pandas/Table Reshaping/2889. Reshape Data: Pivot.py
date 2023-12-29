import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    weather_pivot = weather.pivot(index = 'month', columns = 'city', values = 'temperature')
    return weather_pivot

"""
A pivot table is normally used in data analysis to summarize large dataset. Here we are creating a pivot table with index as month and different cities as columns so
that we can understand the temperature of different cities in each month.
"""
