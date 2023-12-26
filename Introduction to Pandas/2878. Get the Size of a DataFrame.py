import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)

"""
DataFrame.shape return a tuple with the number of rows and number of columns in the dataframe.
"""
