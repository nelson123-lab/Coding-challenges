import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary']*2
    return employees

"""
Here a new column 'bonus' is created with the values of the 'salary' column doubled.
"""
