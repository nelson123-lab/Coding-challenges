import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students

"""
The 'grade' column in the dataframe is converted from float to integer data type.
"""
