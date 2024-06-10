import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    df = pd.concat([df1, df2])
    return df

"""
Here we are concatenating two data frames vertically. Suppose we wish to concatenate the data frames horizontally. It's given below.
df = pd.concat([df1, df2], axis = 1)
"""
