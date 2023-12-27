import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students = students.rename(columns = {
    'id': 'student_id',
    'first': 'first_name',
    'last': 'last_name',
    'age': 'age_in_years'})
    return students

"""
The columns names that are to be replaced are given as a hashmap. Here a python dictionary is used to mention the actual name as key and modified names as the value.
"""
