import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset = 'email', keep = 'first')

"""
drop_duplicates method is used to drop duplicates of rows.
subset = 'email' is where we define the column that we are checking for duplicates.
keep = 'first' is where we define to keep the first occurance of the duplicates.
"""
