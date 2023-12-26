import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset = 'name')

"""
Here we need to define the subset as the 'name' column since we only need to remove the rows if there is any missing value in 'name' column.
"""

import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students[~students['name'].isna()]

"""
The above solution also does the same but here '~' is a bitwise NOT operator in python which inverts the TRUE statement into FALSE thus removing all the
missing values rows of the 'name' column.
"""
