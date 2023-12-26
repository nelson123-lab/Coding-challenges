import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)

"""
The .head method helps in displaying the rows of data from a dataframe. You can choose the number of rows to be displayed.
"""
