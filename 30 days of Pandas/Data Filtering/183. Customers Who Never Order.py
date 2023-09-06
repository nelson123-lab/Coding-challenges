import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    nOrd = pd.merge(customers.rename(columns = {'id': 'customerId', 'name': 'Customers'}), orders, on = 'customerId', how = 'outer')
    filDf = nOrd[nOrd['id'].isnull()]
    return filDf[['Customers']]

"""
Here we need to find the cutomers who never ordered anything this can be found by merging both the table using outer join on 'customerId'. 
Then we can filter the customers data by checking for null values in the order id column. Since they never ordered anything.
"""
