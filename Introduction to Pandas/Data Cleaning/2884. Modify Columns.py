import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary']*2
    return employees

"""
Here the 'salary' column is modified with the doubled value of the salary column.
"""
