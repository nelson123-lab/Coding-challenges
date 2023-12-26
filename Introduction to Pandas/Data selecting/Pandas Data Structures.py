import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns = ['student_id', 'age'])

"""
When we have a nested list of the values the pd.DataFrame function automatically converts them into different columns but if we want names to the columns. We need to mention them in the 
columns attribute of the method.
"""
