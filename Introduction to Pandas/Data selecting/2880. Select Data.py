import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students['student_id'] == 101][['name', 'age']]

"""
Here we are first filtering out all the student_id with the values == 101 and then displaying only the 'name' and 'age' columns of the filtered dataframe.
"""
